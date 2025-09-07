#!/usr/bin/env python3
"""
POLTERGEIST Pure Sally Key System
Made by Samir3632 - No KeyAuth BS!
"""

import json
import secrets
from datetime import datetime, timedelta
import os

class SallyKeyGen:
    def __init__(self):
        # Detectar si estamos en keys/ o en raíz
        if os.path.basename(os.getcwd()) == "keys":
            self.keys_file = "active_keys.json"  # Estamos en keys/
        else:
            self.keys_file = "keys/active_keys.json"  # Estamos en raíz
        
        self.load_keys()
    
    def load_keys(self):
        if os.path.exists(self.keys_file):
            try:
                with open(self.keys_file, 'r') as f:
                    content = f.read().strip()
                    if not content:  # Archivo vacío
                        print("⚠️ Active keys file is empty, creating new database...")
                        self.create_new_db()
                    else:
                        self.keys_db = json.loads(content)
            except json.JSONDecodeError:
                print("⚠️ Corrupted keys file, creating new database...")
                self.create_new_db()
        else:
            print("⚠️ Keys file not found, creating new database...")
            self.create_new_db()
    
    def create_new_db(self):
        # Crear carpeta si no existe
        keys_dir = os.path.dirname(self.keys_file)
        if keys_dir and not os.path.exists(keys_dir):
            os.makedirs(keys_dir, exist_ok=True)
        
        self.keys_db = {
            "metadata": {
                "created": str(datetime.now()),
                "version": "1.0",
                "author": "Samir3632",
                "system": "Sally Pure",
                "total_keys": 0
            },
            "keys": {}
        }
        
        # Agregar keys demo por defecto
        demo_keys = {
            "SALLY-DEMO-1234": {
                "username": "demo_user",
                "created": "2025-01-07 21:23:28",
                "expires": "2025-12-31 23:59:59",
                "type": "demo",
                "status": "active",
                "uses": 0,
                "last_used": None,
                "last_ip": None,
                "created_by": "Samir3632"
            },
            "SALLY-TEST-5678": {
                "username": "test_user", 
                "created": "2025-01-07 21:23:28",
                "expires": "2025-12-31 23:59:59",
                "type": "premium",
                "status": "active",
                "uses": 0,
                "last_used": None,
                "last_ip": None,
                "created_by": "Samir3632"
            },
            "SALLY-PREMIUM-9999": {
                "username": "samir3632",
                "created": "2025-01-07 21:23:28", 
                "expires": "2026-01-07 21:23:28",
                "type": "lifetime",
                "status": "active",
                "uses": 0,
                "last_used": None,
                "last_ip": None,
                "created_by": "Samir3632"
            }
        }
        
        self.keys_db["keys"] = demo_keys
        self.save_keys()
        print("✅ New Sally database created with demo keys!")
    
    def save_keys(self):
        # Asegurar que el directorio existe
        keys_dir = os.path.dirname(self.keys_file)
        if keys_dir and not os.path.exists(keys_dir):
            os.makedirs(keys_dir, exist_ok=True)
        
        self.keys_db["metadata"]["total_keys"] = len(self.keys_db["keys"])
        self.keys_db["metadata"]["last_updated"] = str(datetime.now())
        
        with open(self.keys_file, 'w') as f:
            json.dump(self.keys_db, f, indent=2)
        print(f"💾 Sally database updated - {len(self.keys_db['keys'])} total keys")
        print(f"📁 Saved to: {os.path.abspath(self.keys_file)}")
    
    # ... resto del código igual ...

    def generate_key(self, username, duration_days=30, key_type="premium"):
        # Formato: SALLY-XXXX-XXXX
        prefix = "SALLY"
        part1 = secrets.token_hex(4).upper()
        part2 = secrets.token_hex(4).upper()
        new_key = f"{prefix}-{part1}-{part2}"
        
        # Verificar unicidad
        while new_key in self.keys_db["keys"]:
            part1 = secrets.token_hex(4).upper()
            part2 = secrets.token_hex(4).upper()
            new_key = f"{prefix}-{part1}-{part2}"
        
        # Calcular fechas
        created = datetime.now()
        expires = created + timedelta(days=duration_days)
        
        # Crear entrada
        key_data = {
            "username": username,
            "created": created.strftime("%Y-%m-%d %H:%M:%S"),
            "expires": expires.strftime("%Y-%m-%d %H:%M:%S"),
            "type": key_type,
            "status": "active",
            "uses": 0,
            "last_used": None,
            "last_ip": None,
            "created_by": "Samir3632"
        }
        
        self.keys_db["keys"][new_key] = key_data
        self.save_keys()
        
        print(f"\n🎯 ===== SALLY KEY GENERATED =====")
        print(f"🔑 Key: {new_key}")
        print(f"👤 User: {username}")
        print(f"📅 Created: {key_data['created']}")
        print(f"⏰ Expires: {key_data['expires']}")
        print(f"🏷️ Type: {key_type}")
        print(f"⏳ Duration: {duration_days} days")
        print(f"🎯 ==============================\n")
        
        return new_key

    def validate_key(self, key):
        if key not in self.keys_db["keys"]:
            return {"valid": False, "reason": "Key not found"}
        
        key_data = self.keys_db["keys"][key]
        
        if key_data["status"] != "active":
            return {"valid": False, "reason": "Key disabled"}
        
        # Verificar expiración
        expires = datetime.strptime(key_data["expires"], "%Y-%m-%d %H:%M:%S")
        if datetime.now() > expires:
            key_data["status"] = "expired"
            self.save_keys()
            return {"valid": False, "reason": "Key expired"}
        
        # Key válida - actualizar uso
        key_data["last_used"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        key_data["uses"] += 1
        self.save_keys()
        
        return {
            "valid": True,
            "username": key_data["username"],
            "expires": key_data["expires"],
            "type": key_data["type"],
            "uses": key_data["uses"]
        }

    def list_keys(self, status_filter="all"):
        filtered = {}
        for key, data in self.keys_db["keys"].items():
            if status_filter == "all" or data["status"] == status_filter:
                filtered[key] = data
        
        print(f"\n📋 ===== SALLY KEYS ({status_filter.upper()}) =====")
        print(f"Total: {len(filtered)} keys\n")
        
        for key, data in filtered.items():
            emoji = "✅" if data["status"] == "active" else "❌"
            print(f"{emoji} {key}")
            print(f"   👤 {data['username']} | 🏷️ {data['type']}")
            print(f"   📅 Expires: {data['expires']} | 📊 Uses: {data['uses']}")
            print()

    def bulk_generate(self, count, duration_days=30, key_type="premium"):
        print(f"🚀 Generating {count} Sally keys...")
        keys = []
        for i in range(count):
            username = f"user_{i+1:03d}"
            key = self.generate_key(username, duration_days, key_type)
            keys.append(key)
            if (i+1) % 10 == 0:
                print(f"Progress: {i+1}/{count} keys generated")
        
        print(f"\n✅ {count} keys generated successfully!")
        return keys

    def disable_key(self, key):
        if key in self.keys_db["keys"]:
            self.keys_db["keys"][key]["status"] = "disabled"
            self.save_keys()
            print(f"❌ Key {key} disabled")
            return True
        else:
            print("❌ Key not found")
            return False

    def get_statistics(self):
        total = len(self.keys_db["keys"])
        active = len([k for k, v in self.keys_db["keys"].items() if v["status"] == "active"])
        expired = len([k for k, v in self.keys_db["keys"].items() if v["status"] == "expired"])
        disabled = len([k for k, v in self.keys_db["keys"].items() if v["status"] == "disabled"])
        
        return {
            "total": total,
            "active": active,
            "expired": expired,
            "disabled": disabled
        }

def print_banner():
    print("\n" + "="*60)
    print("🎯 SALLY PURE KEY SYSTEM")
    print("Made by Samir3632 - Unlimited & Free!")
    print("No KeyAuth BS! 🔥")
    print("="*60 + "\n")

def print_menu():
    print("📋 SALLY MENU:")
    print("1. Generate single key")
    print("2. Generate bulk keys")
    print("3. Validate key")
    print("4. List all keys")
    print("5. List active keys")
    print("6. Disable key")
    print("7. Statistics")
    print("8. Exit")

def main():
    print_banner()
    
    try:
        kg = SallyKeyGen()
    except Exception as e:
        print(f"❌ Failed to initialize Sally: {e}")
        return
    
    while True:
        print_menu()
        
        choice = input("\nSelect option: ").strip()
        
        try:
            if choice == "1":
                print("\n🔑 GENERATE SINGLE KEY:")
                username = input("Username: ").strip()
                if not username:
                    print("❌ Username cannot be empty!")
                    continue
                    
                try:
                    duration = int(input("Duration (days) [30]: ") or "30")
                except ValueError:
                    duration = 30
                    print("⚠️ Using default duration: 30 days")
                
                key_type = input("Type [premium]: ").strip() or "premium"
                kg.generate_key(username, duration, key_type)
                
            elif choice == "2":
                print("\n🚀 BULK GENERATE KEYS:")
                try:
                    count = int(input("How many keys: "))
                    if count <= 0:
                        print("❌ Count must be positive!")
                        continue
                    if count > 1000:
                        confirm = input("⚠️ Generating more than 1000 keys. Continue? (y/N): ")
                        if confirm.lower() != 'y':
                            continue
                            
                    duration = int(input("Duration (days) [30]: ") or "30")
                    key_type = input("Type [premium]: ").strip() or "premium"
                    
                    keys = kg.bulk_generate(count, duration, key_type)
                    
                    # Guardar en archivo
                    filename = f"bulk_keys_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                    with open(filename, 'w') as f:
                        for key in keys:
                            f.write(key + "\n")
                    print(f"💾 Keys saved to: {filename}")
                    
                except ValueError:
                    print("❌ Invalid number!")
                    
            elif choice == "3":
                print("\n🔍 VALIDATE KEY:")
                key = input("Enter key to validate: ").strip().upper()
                if not key:
                    print("❌ Key cannot be empty!")
                    continue
                    
                result = kg.validate_key(key)
                print(f"\n📊 VALIDATION RESULT:")
                if result["valid"]:
                    print(f"✅ Key is VALID")
                    print(f"👤 Username: {result['username']}")
                    print(f"⏰ Expires: {result['expires']}")
                    print(f"🏷️ Type: {result['type']}")
                    print(f"📊 Uses: {result['uses']}")
                else:
                    print(f"❌ Key is INVALID")
                    print(f"🔍 Reason: {result['reason']}")
                
            elif choice == "4":
                kg.list_keys("all")
                
            elif choice == "5":
                kg.list_keys("active")
                
            elif choice == "6":
                print("\n🗑️ DISABLE KEY:")
                key = input("Enter key to disable: ").strip().upper()
                if not key:
                    print("❌ Key cannot be empty!")
                    continue
                kg.disable_key(key)
                
            elif choice == "7":
                stats = kg.get_statistics()
                print(f"\n📊 SALLY STATISTICS:")
                print(f"Total Keys: {stats['total']}")
                print(f"✅ Active: {stats['active']}")
                print(f"⏰ Expired: {stats['expired']}")
                print(f"❌ Disabled: {stats['disabled']}")
                
                if stats['total'] > 0:
                    active_percent = (stats['active'] / stats['total']) * 100
                    print(f"📈 Active Rate: {active_percent:.1f}%")
                
            elif choice == "8":
                print("\n👋 Goodbye! Sally system shutting down...")
                break
                
            else:
                print("❌ Invalid option! Please select 1-8.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Sally system shutting down...")
            break
        except Exception as e:
            print(f"❌ Error: {str(e)}")
        
        input("\nPress Enter to continue...")
        print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    main()