import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Definir el nombre del archivo de inventario
archivo_inventario = "Ventas.txt"

# Función para listar productos
def listar_productos():
    with open(archivo_inventario, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print("Código: {}, Nombre: {}, Existencia: {}, Proveedor: {}, Precio: {}".format(*row))

# Función para crear un nuevo producto
def crear_producto(codigo, nombre, existencia, proveedor, precio):
    with open(archivo_inventario, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([codigo, nombre, existencia, proveedor, precio])
    print("Producto creado con éxito.")

#Funcion para actualizar un producto
def actualizar_producto(codigo, nuevo_nombre, nueva_existencia, nuevo_proveedor, nuevo_precio):
    inventario = []
    encontrado = False 

    with open(archivo_inventario, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == codigo:
                row[1] = nuevo_nombre
                row[2] = nueva_existencia
                row[3] = nuevo_proveedor
                row[4] = nuevo_precio
                encontrado = True
            inventario.append(row)

    if encontrado:
        with open(archivo_inventario, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(inventario)
        print("Producto actualizado con éxito.")
    else:
        print("Producto no encontrado.")

#funcion para editar solo la existencia 
def editar_existencia(codigo, nueva_existencia):
    inventario = []
    with open(archivo_inventario, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == codigo:
                row[2] = nueva_existencia
            inventario.append(row)

    with open(archivo_inventario, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(inventario)
    print("Existencia actualizada con éxito.")

#funcion para eliminar un producto 
def eliminar_producto(codigo):
    inventario = []
    with open(archivo_inventario, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != codigo:
                inventario.append(row)

    with open(archivo_inventario, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(inventario)
    print("Producto eliminado con éxito.")

#Aqui empeza la funcion de control de clientes pero no sé si va en esta posición o si debe ir despues del menu que está de ultimo, no sé como debe
#quedar para que pueda hacer el menu de este y que se imprima en la consola por el momento solo cree las funciones pero tengo la duda si debe ir aqui o de ultimo 

control_clientes = "Ventas.txt"

def listar_clientes():
    with open(control_clientes, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print("Código: {}, Nombre: {}, Dirección: {}".format(*row))

def crear_clientes(codigo, nombre, direccion):
    with open(control_clientes, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([codigo, nombre, direccion])
    print("Cliente creado exitosamente.")

def editar_cliente(codigo, nuevo_nombre, nueva_direccion):
     clientes = []
     encontrado = False 

     with open(archivo_inventario, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == codigo:
                row[1] = nuevo_nombre
                row[2] = nueva_direccion
                encontrado = True
            clientes.append(row)

        if encontrado:
            with open(archivo_inventario, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(clientes)
            print("Cliente actualizado con éxito.")
        else:
            print("Cliente no encontrado.")

def eliminar_clientes(codigo):
    clientes = []
    with open(control_clientes, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != codigo:
                clientes.append(row)

    with open(control_clientes, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(clientes)
    print("Cliente eliminado con éxito.")


# 3. Control de ventas 

# Función para generar un reporte en formato CSV o excel
def generar_reporte_csv():
    with open(archivo_inventario, mode='r') as file:
        reader = csv.reader(file)
        with open("reporte.csv", mode='w', newline='') as report_file:
            writer = csv.writer(report_file)
            writer.writerow(["Código", "Nombre", "Existencia", "Proveedor", "Precio"])
            for row in reader:
                writer.writerow(row)
    print("Reporte CSV generado.")

# Funcion para enviar correo
def enviar_correo_con_adjunto(destinatario, asunto, mensaje, archivo_adjunto):
    correo_emisor = '@gmail.com'
    contraseña_emisor = 'tucontraseña'

    msg = MIMEMultipart()
    msg['From'] = correo_emisor
    msg['To'] = destinatario
    msg['Subject'] = asunto

    msg.attach(MIMEText(mensaje, 'plain'))

    with open(archivo_adjunto, "rb") as adjunto:
        part = MIMEApplication(adjunto.read(), Name="reporte.csv")
        part['Content-Disposition'] = f'attachment; filename="{archivo_adjunto}"'
        msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(correo_emisor, contraseña_emisor)
    server.sendmail(correo_emisor, destinatario, msg.as_string())
    server.quit()
    print("Correo enviado con éxito.")

# Ejemplo de uso lo cual es por la consolo 
while True:
    print("\nControl de inventario")
    print("1. Listar productos")
    print("2. Crear producto")
    print("3. Actualizar producto")
    print("4. Editar existencia")
    print("5. Eliminar producto")
    print("6. Generar reporte y enviar por correo")
    print("7. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        listar_productos()
    elif opcion == '2':
        codigo = input("Ingrese el código del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        existencia = input("Ingrese la existencia del producto: ")
        proveedor = input("Ingrese el proveedor del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        crear_producto(codigo, nombre, existencia, proveedor, precio)
    elif opcion == '3':
        codigo = input("Ingrese el código del producto a actualizar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
        nueva_existencia = input("Ingrese la nueva existencia del producto: ")
        nuevo_proveedor = input("Ingrese el nombre del nuevo proveedor: ")
        nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
        actualizar_producto(codigo, nuevo_nombre, nueva_existencia, nuevo_proveedor, nuevo_precio)
    elif opcion == '4':
         codigo = input("Ingrese el código del producto que desea editar: ")
         nueva_existencia = input("Ingrese la nueva existencia del producto: ")
         editar_existencia(codigo, nueva_existencia)
    elif opcion == '5':
         codigo = input("Ingrese el código del producto a eliminar: ")
         eliminar_producto(codigo)
    elif opcion == '6':
         generar_reporte_csv()
         destinatario = input("Ingrese el correo del destinatario: ")
         asunto = "Reporte de inventario"
         mensaje = "Adjunto encontrarás el reporte de inventario."
         archivo_adjunto = "reporte.csv"
         enviar_correo_con_adjunto(destinatario, asunto, mensaje, archivo_adjunto)
    elif opcion == '7':
         print("El programa a finalizado...")
         break
    else:
        print("Opción no válida. Por favor, elige una opción válida.")
