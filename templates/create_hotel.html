<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Yeni Otel Oluştur - YourBookingHub</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        .gradient-bg {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        .file-drop-zone {
            border: 2px dashed #cbd5e0;
            border-radius: 10px;
            transition: all 0.3s ease;
        }
        .file-drop-zone:hover, .file-drop-zone.dragover {
            border-color: #667eea;
            background-color: #f7fafc;
        }
        .upload-preview {
            max-height: 200px;
            overflow-y: auto;
        }
    </style>
</head>
<body class="bg-gray-50">
    <div class="min-h-screen flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
        <div class="max-w-4xl w-full space-y-8">
            <div class="text-center">
                <h2 class="mt-6 text-3xl font-extrabold text-gray-900">
                    🏨 Yeni Otel Hesabı Oluştur
                </h2>
                <p class="mt-2 text-sm text-gray-600">
                    Otelin için kişiselleştirilmiş email otomasyonu
                </p>
            </div>

            <div class="mt-8 gradient-bg rounded-xl shadow-xl p-8">
                <form method="POST" enctype="multipart/form-data" class="space-y-6">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <!-- Hotel Information -->
                        <div class="bg-white rounded-lg p-6 shadow-sm">
                            <h3 class="text-lg font-semibold text-gray-900 mb-4">
                                <i class="fas fa-building text-blue-500 mr-2"></i>
                                Otel Bilgileri
                            </h3>
                            
                            <div class="space-y-4">
                                <div>
                                    <label class="block text-sm font-medium text-gray-700">Otel Adı</label>
                                    <input type="text" name="hotel_name" required
                                           class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
                                           placeholder="Cornelia Diamond Resort & Spa">
                                </div>

                                <div>
                                    <label class="block text-sm font-medium text-gray-700">Domain Adı</label>
                                    <input type="text" name="domain_name" required pattern="[a-zA-Z0-9]+"
                                           class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
                                           placeholder="cornelia">
                                    <p class="mt-1 text-xs text-gray-500">Sadece harf ve rakam</p>
                                </div>
                            </div>
                        </div>

                        <!-- Admin Information -->
                        <div class="bg-white rounded-lg p-6 shadow-sm">
                            <h3 class="text-lg font-semibold text-gray-900 mb-4">
                                <i class="fas fa-user-shield text-green-500 mr-2"></i>
                                Admin Bilgileri
                            </h3>
                            
                            <div class="space-y-4">
                                <div>
                                    <label class="block text-sm font-medium text-gray-700">Admin Email</label>
                                    <input type="email" name="admin_email" required
                                           class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
                                           placeholder="admin@corneliahotel.com">
                                </div>

                                <div>
                                    <label class="block text-sm font-medium text-gray-700">Admin Şifre</label>
                                    <input type="password" name="admin_password" required
                                           class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
                                           placeholder="Güvenli şifre oluşturun">
                                </div>

                                <div>
                                    <label class="block text-sm font-medium text-gray-700">Gmail Hesabı</label>
                                    <input type="email" name="gmail_email"
                                           class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500"
                                           placeholder="booking@corneliahotel.com">
                                    <p class="mt-1 text-xs text-gray-500">Email almak için kullanılacak Gmail</p>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- File Upload Section -->
                    <div class="bg-white rounded-lg p-6 shadow-sm">
                        <h3 class="text-lg font-semibold text-gray-900 mb-4">
                            <i class="fas fa-upload text-purple-500 mr-2"></i>
                            Dosya/Klasör Yükleme (app_complete.py dahil)
                        </h3>
                        
                        <!-- Upload Type Selection -->
                        <div class="mb-4 flex space-x-4">
                            <label class="flex items-center">
                                <input type="radio" name="upload_type" value="files" checked class="mr-2">
                                <i class="fas fa-file mr-1"></i> Dosya Yükle
                            </label>
                            <label class="flex items-center">
                                <input type="radio" name="upload_type" value="folder" class="mr-2">
                                <i class="fas fa-folder mr-1"></i> Klasör Yükle
                            </label>
                        </div>
                        
                        <div class="file-drop-zone p-8 text-center" id="dropZone">
                            <i class="fas fa-cloud-upload-alt text-4xl text-gray-400 mb-4"></i>
                            <p class="text-lg font-medium text-gray-700 mb-2">
                                Dosyaları/Klasörü buraya sürükleyin veya tıklayın
                            </p>
                            <p class="text-sm text-gray-500 mb-2">
                                Python dosyaları (.py), resimler, HTML template'leri, dökümanlar
                            </p>
                            <p class="text-xs text-red-500 mb-4">
                                <i class="fas fa-exclamation-triangle mr-1"></i>
                                Maksimum 100 MB sınırı
                            </p>
                            
                            <!-- File Input for Files -->
                            <input type="file" name="files" multiple id="fileInput" class="hidden"
                                   accept=".py,.html,.jpg,.jpeg,.png,.gif,.pdf,.doc,.docx,.txt,.js,.css,.json,.env">
                            
                            <!-- Directory Input for Folders -->
                            <input type="file" name="folder_files" multiple id="folderInput" class="hidden"
                                   webkitdirectory directory>
                            
                            <div class="space-x-3">
                                <button type="button" id="fileButton"
                                        class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-lg transition duration-200">
                                    <i class="fas fa-file mr-2"></i>
                                    Dosya Seç
                                </button>
                                <button type="button" id="folderButton" style="display:none;"
                                        class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-lg transition duration-200">
                                    <i class="fas fa-folder mr-2"></i>
                                    Klasör Seç
                                </button>
                            </div>
                        </div>

                        <!-- File Preview -->
                        <div id="filePreview" class="upload-preview mt-4 hidden">
                            <div class="flex justify-between items-center mb-2">
                                <h4 class="text-sm font-medium text-gray-700">Yüklenecek Dosyalar:</h4>
                                <div id="totalSize" class="text-xs text-gray-500"></div>
                            </div>
                            <div id="fileList" class="space-y-2 max-h-48 overflow-y-auto"></div>
                            <div id="sizeWarning" class="text-red-500 text-sm mt-2 hidden">
                                <i class="fas fa-exclamation-triangle mr-1"></i>
                                Toplam dosya boyutu 100 MB'ı aşıyor!
                            </div>
                        </div>
                    </div>

                    <!-- Submit Button -->
                    <div class="flex justify-center">
                        <button type="submit" 
                                class="group relative w-full md:w-auto flex justify-center py-3 px-8 border border-transparent text-lg font-medium rounded-xl text-white bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition duration-200 transform hover:scale-105">
                            <i class="fas fa-plus-circle mr-2"></i>
                            Otel Hesabı Oluştur
                        </button>
                    </div>
                </form>
            </div>

            <div class="text-center">
                <a href="/admin/dashboard" class="text-blue-600 hover:text-blue-800 font-medium">
                    <i class="fas fa-arrow-left mr-2"></i>
                    Admin Panel'e Dön
                </a>
            </div>
        </div>
    </div>

    <script>
        // File upload functionality
        const dropZone = document.getElementById('dropZone');
        const fileInput = document.getElementById('fileInput');
        const folderInput = document.getElementById('folderInput');
        const filePreview = document.getElementById('filePreview');
        const fileList = document.getElementById('fileList');
        const fileButton = document.getElementById('fileButton');
        const folderButton = document.getElementById('folderButton');
        const totalSizeDiv = document.getElementById('totalSize');
        const sizeWarning = document.getElementById('sizeWarning');
        
        const MAX_SIZE = 100 * 1024 * 1024; // 100 MB in bytes
        let currentFiles = [];

        // Upload type radio buttons
        document.querySelectorAll('input[name="upload_type"]').forEach(radio => {
            radio.addEventListener('change', (e) => {
                if (e.target.value === 'files') {
                    fileButton.style.display = 'inline-block';
                    folderButton.style.display = 'none';
                    currentFiles = [];
                    updateFilePreview([]);
                } else {
                    fileButton.style.display = 'none';
                    folderButton.style.display = 'inline-block';
                    currentFiles = [];
                    updateFilePreview([]);
                }
            });
        });

        // Button click handlers
        fileButton.addEventListener('click', () => fileInput.click());
        folderButton.addEventListener('click', () => folderInput.click());

        // Drag and drop
        dropZone.addEventListener('dragover', (e) => {
            e.preventDefault();
            dropZone.classList.add('dragover');
        });

        dropZone.addEventListener('dragleave', () => {
            dropZone.classList.remove('dragover');
        });

        dropZone.addEventListener('drop', (e) => {
            e.preventDefault();
            dropZone.classList.remove('dragover');
            
            const files = Array.from(e.dataTransfer.files);
            currentFiles = files;
            updateFilePreview(files);
        });

        // File input changes
        fileInput.addEventListener('change', (e) => {
            currentFiles = Array.from(e.target.files);
            updateFilePreview(currentFiles);
        });

        folderInput.addEventListener('change', (e) => {
            currentFiles = Array.from(e.target.files);
            updateFilePreview(currentFiles);
        });

        function updateFilePreview(files) {
            fileList.innerHTML = '';
            
            if (files.length === 0) {
                filePreview.classList.add('hidden');
                return;
            }
            
            filePreview.classList.remove('hidden');
            
            let totalSize = 0;
            const filesByFolder = {};
            
            files.forEach(file => {
                totalSize += file.size;
                
                // Group files by folder for better organization
                const path = file.webkitRelativePath || file.name;
                const folder = path.includes('/') ? path.split('/')[0] : 'Ana Klasör';
                
                if (!filesByFolder[folder]) {
                    filesByFolder[folder] = [];
                }
                filesByFolder[folder].push(file);
            });
            
            // Display total size
            const sizeText = formatFileSize(totalSize);
            totalSizeDiv.textContent = `Toplam: ${sizeText}`;
            
            // Show warning if over 100MB
            if (totalSize > MAX_SIZE) {
                sizeWarning.classList.remove('hidden');
                totalSizeDiv.classList.add('text-red-500');
            } else {
                sizeWarning.classList.add('hidden');
                totalSizeDiv.classList.remove('text-red-500');
            }
            
            // Display files grouped by folder
            Object.keys(filesByFolder).forEach(folderName => {
                if (Object.keys(filesByFolder).length > 1) {
                    const folderHeader = document.createElement('div');
                    folderHeader.className = 'font-medium text-gray-700 mt-3 mb-1 flex items-center';
                    folderHeader.innerHTML = `
                        <i class="fas fa-folder text-yellow-500 mr-2"></i>
                        ${folderName} (${filesByFolder[folderName].length} dosya)
                    `;
                    fileList.appendChild(folderHeader);
                }
                
                filesByFolder[folderName].forEach(file => {
                    const fileItem = document.createElement('div');
                    fileItem.className = 'flex items-center justify-between bg-gray-50 p-2 rounded ml-4';
                    
                    const fileIcon = getFileIcon(file.name);
                    const fileSize = formatFileSize(file.size);
                    
                    fileItem.innerHTML = `
                        <div class="flex items-center">
                            <i class="${fileIcon} mr-2"></i>
                            <span class="text-sm">${file.name}</span>
                        </div>
                        <span class="text-xs text-gray-500">${fileSize}</span>
                    `;
                    
                    fileList.appendChild(fileItem);
                });
            });
        }

        function formatFileSize(bytes) {
            if (bytes === 0) return '0 Bytes';
            const k = 1024;
            const sizes = ['Bytes', 'KB', 'MB', 'GB'];
            const i = Math.floor(Math.log(bytes) / Math.log(k));
            return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
        }

        function getFileIcon(filename) {
            const ext = filename.split('.').pop().toLowerCase();
            const iconMap = {
                'py': 'fas fa-code text-blue-500',
                'html': 'fab fa-html5 text-orange-500',
                'css': 'fab fa-css3-alt text-blue-400',
                'js': 'fab fa-js-square text-yellow-500',
                'json': 'fas fa-brackets-curly text-green-500',
                'txt': 'fas fa-file-text text-gray-500',
                'pdf': 'fas fa-file-pdf text-red-500',
                'doc': 'fas fa-file-word text-blue-600',
                'docx': 'fas fa-file-word text-blue-600',
                'jpg': 'fas fa-image text-purple-500',
                'jpeg': 'fas fa-image text-purple-500',
                'png': 'fas fa-image text-purple-500',
                'gif': 'fas fa-image text-purple-500',
                'env': 'fas fa-cog text-gray-600'
            };
            return iconMap[ext] || 'fas fa-file text-gray-400';
        }

        // Form submission with file size validation
        document.querySelector('form').addEventListener('submit', function(e) {
            let totalSize = 0;
            currentFiles.forEach(file => totalSize += file.size);
            
            if (totalSize > MAX_SIZE) {
                e.preventDefault();
                alert(`Dosya boyutu çok büyük! Maksimum ${formatFileSize(MAX_SIZE)} yükleyebilirsiniz.`);
                return false;
            }
            
            if (currentFiles.length === 0) {
                const proceed = confirm('Hiç dosya seçmediniz. Yine de devam etmek istiyor musunuz?');
                if (!proceed) {
                    e.preventDefault();
                    return false;
                }
            }
        });
    </script>
</body>
</html>