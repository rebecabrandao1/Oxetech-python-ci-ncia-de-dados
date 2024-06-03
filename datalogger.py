import serial
import threading

porta = "COM4"
baud = 9600
arquivo = "datalogger.csv"

ser = serial.Serial(porta, baud)
ser.flushInput()
print("*******************Abrindo Serial...**********************")
stop_flag = False

def aguardar_tecla():
    global stop_flag
    input("Pressione Enter para parar...\n")
    stop_flag = True

thread = threading.Thread(target=aguardar_tecla)
thread.start()

while not stop_flag:
    data = str(ser.readline().decode("utf-8"))
    print(data)
    with open(arquivo, "a") as file:
        file.write(data)

print("*******************Finalizando leitura****************")
ser.close() 