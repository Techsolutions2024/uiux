from services.database import get_db_connection

def get_devices():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM devices")
    devices = [{"id": row[0], "name": row[1], "ip": row[2], "status": row[3]} for row in c.fetchall()]
    conn.close()
    return devices

def add_device(name, ip):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO devices (name, ip, status) VALUES (?, ?, ?)", (name, ip, True))
    conn.commit()
    conn.close()

def delete_device(device_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM devices WHERE id = ?", (device_id,))
    conn.commit()
    conn.close()