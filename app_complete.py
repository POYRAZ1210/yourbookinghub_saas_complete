# -*- coding: utf-8 -*-
import os
import threading
import time
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from gmail_service import GmailService
from email_processor import EmailProcessor
from database import CorneliaDatabase
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'cornelia-secret-key-2025')

# Initialize services
gmail_service = GmailService()
email_processor = EmailProcessor()
db_manager = CorneliaDatabase()

# Global variables for email processing
processing_active = False
processing_thread = None

@app.route('/')
def index():
    """Cornelia Diamond Resort website"""
    return render_template('cornelia_website.html')

@app.route('/dashboard')
def dashboard():
    """Main dashboard page"""
    try:
        # Check if Gmail is authenticated
        is_authenticated = gmail_service.is_authenticated()
        
        # Get recent activity from database
        recent_emails = []
        if is_authenticated:
            try:
                recent_emails = db_manager.get_customer_history('all', limit=10)
            except:
                recent_emails = []
        
        # Get system stats
        stats = {
            'total_processed': len(recent_emails),
            'today_processed': len([e for e in recent_emails if 'today' in str(e.get('processed_at', ''))]),
            'pending_emails': 0,
            'processing_active': processing_active
        }
        
        if is_authenticated:
            try:
                pending_emails = gmail_service.get_unread_emails(max_results=5)
                stats['pending_emails'] = len(pending_emails)
            except:
                stats['pending_emails'] = 0
        
        return render_template('dashboard.html', 
                             is_authenticated=is_authenticated,
                             recent_emails=recent_emails[:10],
                             stats=stats)
    except Exception as e:
        logger.error(f"Error loading dashboard: {str(e)}")
        return render_template('dashboard.html', 
                             is_authenticated=False,
                             recent_emails=[],
                             stats={'total_processed': 0, 'today_processed': 0, 'pending_emails': 0, 'processing_active': False},
                             error=str(e))

@app.route('/auth/gmail')
def auth_gmail():
    """Initiate Gmail OAuth flow"""
    try:
        auth_url = gmail_service.get_auth_url()
        return redirect(auth_url)
    except Exception as e:
        logger.error(f"Error initiating Gmail auth: {str(e)}")
        return redirect(url_for('index'))

@app.route('/auth/callback')
def auth_callback():
    """Handle Gmail OAuth callback"""
    try:
        code = request.args.get('code')
        if code:
            success = gmail_service.handle_auth_callback(code)
            if success:
                logger.info("Gmail authentication successful")
            else:
                logger.error("Gmail authentication failed")
        return redirect(url_for('index'))
    except Exception as e:
        logger.error(f"Error handling auth callback: {str(e)}")
        return redirect(url_for('index'))

@app.route('/api/start-processing', methods=['POST'])
def start_processing():
    """Start automated email processing"""
    global processing_active, processing_thread
    
    try:
        if not gmail_service.is_authenticated():
            return jsonify({'success': False, 'error': 'Gmail not authenticated'})
        
        if processing_active:
            return jsonify({'success': False, 'error': 'Processing already active'})
        
        processing_active = True
        processing_thread = threading.Thread(target=email_processing_loop)
        processing_thread.daemon = True
        processing_thread.start()
        
        logger.info("Email processing started")
        return jsonify({'success': True, 'message': 'Email processing started'})
    
    except Exception as e:
        logger.error(f"Error starting processing: {str(e)}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/stop-processing', methods=['POST'])
def stop_processing():
    """Stop automated email processing"""
    global processing_active
    
    try:
        processing_active = False
        logger.info("Email processing stopped")
        return jsonify({'success': True, 'message': 'Email processing stopped'})
    
    except Exception as e:
        logger.error(f"Error stopping processing: {str(e)}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/stats')
def get_stats():
    """Get current system statistics"""
    try:
        stats = {
            'processing_active': processing_active,
            'gmail_authenticated': gmail_service.is_authenticated()
        }
        
        # Get database stats if available
        try:
            db_stats = db_manager.get_system_statistics()
            stats.update(db_stats)
        except:
            stats.update({
                'total_emails': 0,
                'responses_sent': 0,
                'today_count': 0
            })
        
        # Get pending emails count
        if gmail_service.is_authenticated():
            try:
                pending_emails = gmail_service.get_unread_emails(max_results=5)
                stats['pending_emails'] = len(pending_emails)
            except:
                stats['pending_emails'] = 0
        else:
            stats['pending_emails'] = 0
            
        return jsonify(stats)
    except Exception as e:
        logger.error(f"Error getting stats: {str(e)}")
        return jsonify({'error': str(e)})

def email_processing_loop():
    """Main email processing loop with GPT analysis"""
    global processing_active
    
    logger.info("Email processing loop started with GPT analysis")
    
    while processing_active:
        try:
            if not gmail_service.is_authenticated():
                logger.warning("Gmail not authenticated, stopping processing")
                processing_active = False
                break
            
            # Get unread emails
            unread_emails = gmail_service.get_unread_emails(max_results=10)
            logger.info(f"Found {len(unread_emails)} unread emails")
            
            for email_data in unread_emails:
                if not processing_active:
                    break
                
                try:
                    email_id = email_data['id']
                    sender = email_data['sender']
                    subject = email_data['subject']
                    body = email_data['body']
                    
                    logger.info(f"Processing email from {sender}: {subject}")
                    
                    # Process email with GPT analysis
                    result = email_processor.process_email(email_data)
                    
                    if result['success']:
                        # Send response
                        response_sent = gmail_service.send_response(
                            sender,
                            result['subject'],
                            result['response_html']
                        )
                        
                        # Log to database
                        try:
                            email_record = {
                                'gmail_message_id': email_id,
                                'customer_email': sender,
                                'subject': subject,
                                'email_content': body,
                                'detected_language': result.get('language', 'en'),
                                'response_sent': response_sent,
                                'response_type': 'gpt_analysis',
                                'processing_time_ms': 1000,
                                'received_at': email_data.get('timestamp', '')
                            }
                            
                            # Add analysis data
                            analysis = result.get('analysis', {})
                            email_record.update({
                                'adults': analysis.get('adults', 0),
                                'children': analysis.get('children', 0),
                                'room_type': analysis.get('room_type', ''),
                                'information_complete': analysis.get('is_complete', False)
                            })
                            
                            db_manager.save_customer_email(email_record)
                        except Exception as db_error:
                            logger.error(f"Database save error: {db_error}")
                        
                        # Mark as read
                        gmail_service.mark_as_read(email_id)
                        
                        logger.info(f"Successfully processed email from {sender}")
                    else:
                        logger.error(f"Failed to process email from {sender}: {result.get('error', 'Unknown error')}")
                    
                except Exception as e:
                    logger.error(f"Error processing email {email_data.get('id', 'unknown')}: {str(e)}")
                    continue
            
            # Wait before next check
            time.sleep(30)  # Check every 30 seconds
            
        except Exception as e:
            logger.error(f"Error in processing loop: {str(e)}")
            time.sleep(60)  # Wait longer on error
    
    logger.info("Email processing loop stopped")

@app.route('/test-system')
def test_system():
    """Test system components"""
    test_results = {
        'gmail_service': False,
        'email_processor': False,
        'database': False,
        'openai': False
    }
    
    # Test Gmail service
    try:
        test_results['gmail_service'] = gmail_service.is_authenticated()
    except:
        pass
    
    # Test email processor
    try:
        if email_processor.openai_client:
            test_results['openai'] = True
        if email_processor.hotel_system:
            test_results['email_processor'] = True
    except:
        pass
    
    # Test database
    try:
        db_manager.get_system_statistics()
        test_results['database'] = True
    except:
        pass
    
    return jsonify(test_results)

@app.route('/api/test-email', methods=['POST'])
def test_email_processing():
    """Test email processing with John Smith message"""
    try:
        # John Smith'in mesajı - GPT analizini test edelim
        john_smith_email = {
            'id': 'test_john_smith_' + str(int(time.time())),
            'sender': 'john.smith@example.com',
            'subject': 'Booking Inquiry - Cornelia Diamond',
            'body': '''Hello,

I would like to inquire about availability and pricing for a stay at Cornelia Diamond.
We are 2 adults and 2 children (ages 13 and 6).
We are planning to stay from August 10th to August 15th, and we are interested in a suite room.

Could you please provide the total price and more details about the room and hotel facilities?

Thank you in advance.

Best regards,
John Smith''',
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')
        }
        
        logger.info("Testing John Smith email with GPT analysis")
        
        # Email processor ile analiz et
        result = email_processor.process_email(john_smith_email)
        
        if result['success']:
            analysis = result.get('analysis', {})
            
            # Sonuçları logla
            logger.info(f"✅ Analysis complete - Method: {analysis.get('analysis_method', 'unknown')}")
            logger.info(f"📅 Dates detected: {analysis.get('dates', 'None')}")
            logger.info(f"👥 Guests: {analysis.get('adults', 0)} adults + {analysis.get('children', 0)} children")
            logger.info(f"🌙 Nights: {analysis.get('nights', 0)}")
            logger.info(f"🏨 Room: {analysis.get('room_type', 'unknown')}")
            
            return jsonify({
                'success': True,
                'message': 'John Smith email processed successfully',
                'email_data': {
                    'sender': john_smith_email['sender'],
                    'subject': john_smith_email['subject']
                },
                'analysis_result': {
                    'guest_name': analysis.get('guest_name', 'Not detected'),
                    'adults': analysis.get('adults', 0),
                    'children': analysis.get('children', 0), 
                    'nights': analysis.get('nights', 0),
                    'room_type': analysis.get('room_type', 'unknown'),
                    'dates': analysis.get('dates', 'Not detected'),
                    'check_in': analysis.get('check_in', 'Not detected'),
                    'check_out': analysis.get('check_out', 'Not detected'),
                    'analysis_method': analysis.get('analysis_method', 'unknown'),
                    'api_used': analysis.get('analysis_method') == 'gpt_analysis'
                },
                'language': result.get('language', 'en'),
                'response_generated': len(result.get('response_html', '')) > 0
            })
        else:
            return jsonify({
                'success': False,
                'error': result.get('error', 'Unknown error'),
                'message': 'Failed to process John Smith email'
            })
        
    except Exception as e:
        logger.error(f"Test email processing error: {e}")
        return jsonify({
            'success': False,
            'error': str(e),
            'message': 'Exception during test email processing'
        })

if __name__ == '__main__':
    # Initialize database
    try:
        db_manager.init_database()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Database initialization failed: {e}")
    
    # Start Flask app
    logger.info("Starting Cornelia Diamond Email Automation Dashboard")
    logger.info("Dashboard will be available at: http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)