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
        self.keys_file = "active_keys.json"
        self.load_keys()
    
    def load_keys(self):
        if os.path.exists(self.keys_file):
            with open(self.keys_file, 'r') as f:
                self.keys_db = json.load(f)
        else:
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
    
    def save_keys(self):
        self.keys_db["metadata"]["total_keys"] = len(self.keys_db["keys"])
        self.keys_db["metadata"]["last_updated"] = str(datetime.now())
        with open(self.keys_file, 'w') as f:
            json.dump(self.keys_db, f, indent=2)
        print(f"💾 Sally database updated - {len(self.keys_db['keys'])} total keys")
    
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

def main():
    kg = SallyKeyGen()
    
    print("🎯 SALLY PURE KEY SYSTEM")
    print("Made by Samir3632 - Unlimited & Free!")
    print("No KeyAuth BS! 🔥\n")
    
    while True:
        print("📋 SALLY MENU:")
        print("1. Generate single key")
        print("2. Generate bulk keys")
        print("3. Validate key")
        print("4. List all keys")
        print("5. List active keys")
        print("6. Disable key")
        print("7. Statistics")
        print("8. Exit")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == "1":
            username = input("Username: ").strip()
            duration = int(input("Duration (days) [30]: ") or "30")
            key_type = input("Type [premium]: ").strip() or "premium"
            kg.generate_key(username, duration, key_type)
            
        elif choice == "2":
            count = int(input("How many keys: "))
            duration = int(input("Duration (days) [30]: ") or "30")
            key_type = input("Type [premium]: ").strip() or "premium"
            keys = kg.bulk_generate(count, duration, key_type)
            
            # Guardar en archivo
            with open(f"bulk_keys_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt", 'w') as f:
                for key in keys:
                    f.write(key + "\n")
            print(f"Keys saved to bulk_keys file!")
            
        elif choice == "3":
            key = input("Enter key to validate: ").strip()
            result = kg.validate_key(key)
            print(f"Result: {result}")
            
        elif choice == "4":
            kg.list_keys("all")
            
        elif choice == "5":
            kg.list_keys("active")
            
        elif choice == "6":
            key = input("Enter key to disable: ").strip()
            if key in kg.keys_db["keys"]:
                kg.keys_db["keys"][key]["status"] = "disabled"
                kg.save_keys()
                print(f"❌ Key {key} disabled")
            else:
                print("Key not found")
                
        elif choice == "7":
            total = len(kg.keys_db["keys"])
            active = len([k for k, v in kg.keys_db["keys"].items() if v["status"] == "active"])
            expired = len([k for k, v in kg.keys_db["keys"].items() if v["status"] == "expired"])
            disabled = len([k for k, v in kg.keys_db["keys"].items() if v["status"] == "disabled"])
            
            print(f"\n📊 SALLY STATISTICS:")
            print(f"Total Keys: {total}")
            print(f"Active: {active}")
            print(f"Expired: {expired}")
            print(f"Disabled: {disabled}")
            
        elif choice == "8":
            break
        
        input("\nPress Enter to continue...")
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()