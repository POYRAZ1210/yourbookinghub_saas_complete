from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
import os
from datetime import datetime
import secrets

app = Flask(__name__, template_folder='../templates')
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev-key-for-testing')

# In-memory storage for demo
hotels_db = {
    'cornelia': {
        'name': 'Cornelia Diamond Resort & Spa',
        'city': 'Antalya, Turkey',
        'theme_color': '#D4AF37',
        'admin_username': 'admin',
        'admin_password': 'admin123',
        'gmail_account': None,
        'system_status': 'stopped'
    },
    'rixos': {
        'name': 'Rixos Premium Belek',
        'city': 'Belek, Turkey',
        'theme_color': '#1E40AF',
        'admin_username': 'admin',
        'admin_password': 'admin123',
        'gmail_account': None,
        'system_status': 'stopped'
    }
}

admin_credentials = {'username': 'admin', 'password': 'admin123'}

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'YourBookingHub.org'
    })

@app.route('/admin')
def admin_login():
    return render_template('admin_login.html')

@app.route('/admin/login', methods=['POST'])
def admin_login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == admin_credentials['username'] and password == admin_credentials['password']:
        session['admin_logged_in'] = True
        return redirect(url_for('admin_dashboard'))
    else:
        flash('Invalid credentials')
        return redirect(url_for('admin_login'))

@app.route('/admin/dashboard')
def admin_dashboard():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    return render_template('admin_dashboard.html', hotels=hotels_db)

@app.route('/admin/create_hotel')
def admin_create_hotel():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    return render_template('admin_create_hotel.html')

@app.route('/admin/create_hotel', methods=['POST'])
def admin_create_hotel_post():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    hotel_name = request.form.get('hotel_name')
    hotel_domain = request.form.get('hotel_domain')
    
    if not hotel_domain or not hotel_domain.isalnum():
        flash('Invalid domain name')
        return redirect(url_for('admin_create_hotel'))
    
    if hotel_domain in hotels_db:
        flash('Domain already exists')
        return redirect(url_for('admin_create_hotel'))
    
    hotels_db[hotel_domain] = {
        'name': hotel_name,
        'city': request.form.get('hotel_city', ''),
        'theme_color': request.form.get('theme_color', '#3B82F6'),
        'admin_username': request.form.get('admin_username', 'admin'),
        'admin_password': request.form.get('admin_password', 'admin123'),
        'gmail_account': None,
        'system_status': 'stopped'
    }
    
    flash(f'Hotel {hotel_name} created successfully')
    return redirect(url_for('admin_dashboard'))

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('homepage'))

@app.route('/hotel/<domain>')
def hotel_login(domain):
    if domain not in hotels_db:
        return render_template('404.html'), 404
    hotel = hotels_db[domain]
    return render_template('hotel_login.html', hotel=hotel, domain=domain)

@app.route('/hotel/<domain>/login', methods=['POST'])
def hotel_login_post(domain):
    if domain not in hotels_db:
        return render_template('404.html'), 404
    
    hotel = hotels_db[domain]
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == hotel['admin_username'] and password == hotel['admin_password']:
        session[f'hotel_{domain}_logged_in'] = True
        return redirect(url_for('hotel_dashboard', domain=domain))
    else:
        flash('Invalid credentials')
        return redirect(url_for('hotel_login', domain=domain))

@app.route('/hotel/<domain>/dashboard')
def hotel_dashboard(domain):
    if domain not in hotels_db:
        return render_template('404.html'), 404
    if not session.get(f'hotel_{domain}_logged_in'):
        return redirect(url_for('hotel_login', domain=domain))
    hotel = hotels_db[domain]
    return render_template('hotel_dashboard.html', hotel=hotel, domain=domain)

@app.route('/hotel/<domain>/gmail/connect', methods=['POST'])
def hotel_gmail_connect(domain):
    if domain not in hotels_db or not session.get(f'hotel_{domain}_logged_in'):
        return jsonify({'error': 'Not authorized'}), 401
    
    hotels_db[domain]['gmail_account'] = 'demo@gmail.com'
    return jsonify({'success': True, 'message': 'Gmail connected successfully'})

@app.route('/hotel/<domain>/system/start', methods=['POST'])
def hotel_system_start(domain):
    if domain not in hotels_db or not session.get(f'hotel_{domain}_logged_in'):
        return jsonify({'error': 'Not authorized'}), 401
    
    hotels_db[domain]['system_status'] = 'running'
    return jsonify({'success': True, 'status': 'running'})

@app.route('/hotel/<domain>/system/stop', methods=['POST'])
def hotel_system_stop(domain):
    if domain not in hotels_db or not session.get(f'hotel_{domain}_logged_in'):
        return jsonify({'error': 'Not authorized'}), 401
    
    hotels_db[domain]['system_status'] = 'stopped'
    return jsonify({'success': True, 'status': 'stopped'})

@app.route('/hotel/<domain>/logout')
def hotel_logout(domain):
    session.pop(f'hotel_{domain}_logged_in', None)
    return redirect(url_for('hotel_login', domain=domain))

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)