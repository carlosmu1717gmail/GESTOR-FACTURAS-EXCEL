import hashlib
import json
import os
from pathlib import Path
from datetime import datetime

CACHE_FILE = "cache_facturas.json"

class CacheManager:
    """Gestiona caché de facturas procesadas por hash de contenido"""
    
    def __init__(self):
        self.cache = self._load_cache()
    
    def _load_cache(self):
        """Carga el caché desde archivo"""
        if os.path.exists(CACHE_FILE):
            try:
                with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def _save_cache(self):
        """Guarda el caché en archivo"""
        try:
            with open(CACHE_FILE, 'w', encoding='utf-8') as f:
                json.dump(self.cache, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"⚠️ No se pudo guardar caché: {e}")
    
    def get_file_hash(self, file_path):
        """Calcula SHA-256 del contenido del archivo"""
        sha256 = hashlib.sha256()
        try:
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    sha256.update(chunk)
            return sha256.hexdigest()
        except:
            return None
    
    def get_cached_data(self, file_path):
        """Obtiene datos cacheados si existen"""
        file_hash = self.get_file_hash(file_path)
        if file_hash and file_hash in self.cache:
            cached_entry = self.cache[file_hash]
            # Actualizar nombre de archivo (puede haber cambiado)
            cached_data = cached_entry.get('data', {})
            cached_data['file_name'] = Path(file_path).name
            return cached_data
        return None
    
    def save_to_cache(self, file_path, data):
        """Guarda datos en caché"""
        file_hash = self.get_file_hash(file_path)
        if file_hash:
            self.cache[file_hash] = {
                'data': data,
                'processed_at': datetime.now().isoformat(),
                'file_name': Path(file_path).name
            }
            self._save_cache()
    
    def is_cached(self, file_path):
        """Verifica si un archivo está en caché"""
        file_hash = self.get_file_hash(file_path)
        return file_hash and file_hash in self.cache
    
    def clear_cache(self):
        """Limpia todo el caché"""
        self.cache = {}
        self._save_cache()
        if os.path.exists(CACHE_FILE):
            os.remove(CACHE_FILE)
