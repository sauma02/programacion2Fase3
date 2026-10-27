import tkinter as tk
from tkinter import simpledialog
from servicios.ServicioCrearFigura import ServicioCrearFigura


class main:
    def __init__(self, ventana):
        self.ventana = ventana
        self.servicio = ServicioCrearFigura()

        ventana.title("Sistema de modelado de figuras 3D")
        ventana.geometry("620x420")

        tk.Label(
            ventana,
            text="Bienvenido al sistema de modelado de figuras 3d,\nporfavor seleccione una de las siguientes opciones",
        ).pack(pady=10)

        # Menu principal (mismas opciones que en consola)
        tk.Button(ventana, text="1- Crear una figura", width=30, command=self.opcion1).pack(pady=2)
        tk.Button(ventana, text="2- Mostrar figuras registradas", width=30, command=self.opcion2).pack(pady=2)
        tk.Button(ventana, text="3- Mostrar figuras y sus valores", width=30, command=self.opcion3).pack(pady=2)
        tk.Button(ventana, text="4- Salir", width=30, command=self.opcion4).pack(pady=2)

        # Aqui van los "print" de antes
        self.salida = tk.Text(ventana, height=12, state="disabled")
        self.salida.pack(fill="both", expand=True, padx=10, pady=10)

    # ---------- utilidades ----------
    def escribir(self, texto, limpiar=False):
        """Reemplaza al print()."""
        self.salida.config(state="normal")
        if limpiar:
            self.salida.delete("1.0", tk.END)
        self.salida.insert(tk.END, texto + "\n")
        self.salida.config(state="disabled")

    def pedir(self, mensaje):
        """Reemplaza al float(input(...)). Devuelve None si se cancela."""
        return simpledialog.askfloat("Ingrese un valor", mensaje, parent=self.ventana, minvalue=0.0001)

    # ---------- opcion 1: crear figura ----------
    def opcion1(self):
        menu = tk.Toplevel(self.ventana)
        menu.title("Crear figura")
        menu.geometry("260x200")
        menu.grab_set()

        tk.Label(menu, text="¿Que figura desea crear?").pack(pady=8)
        tk.Button(menu, text="1- Esfera", width=20, command=self.crearEsfera).pack(pady=2)
        tk.Button(menu, text="2- Cubo", width=20, command=self.crearCubo).pack(pady=2)
        tk.Button(menu, text="3- Cilindro", width=20, command=self.crearCilindro).pack(pady=2)
        tk.Button(menu, text="4- Volver", width=20, command=menu.destroy).pack(pady=2)

    def crearEsfera(self):
        radio = self.pedir("Ingrese el valor del radio.")
        if radio is None:
            return
        escalar = self.pedir("Ingrese el valor de la escala a la cual se hara el calculo de la figura")
        if escalar is None:
            return
        esfera = self.servicio.crearEsfera(radio, escalar)
        self.escribir(f"Esfera creada: {esfera.dibujar()} con escalar {escalar}", limpiar=True)

    def crearCubo(self):
        lado = self.pedir("Ingrese el valor de uno de los lados.")
        if lado is None:
            return
        escalar = self.pedir("Ingrese el valor de la escala a la cual se hara el calculo de la figura")
        if escalar is None:
            return
        cubo = self.servicio.crearCubo(lado, escalar)
        self.escribir(f"Cubo creado: {cubo.dibujar()} con escalar {escalar}", limpiar=True)

    def crearCilindro(self):
        radio = self.pedir("Ingrese el valor del radio.")
        if radio is None:
            return
        altura = self.pedir("Ingrese el valor de la altura.")
        if altura is None:
            return
        escalar = self.pedir("Ingrese el valor de la escala a la cual se hara el calculo de la figura")
        if escalar is None:
            return
        cilindro = self.servicio.crearCilindro(radio, altura, escalar)
        self.escribir(f"Cilindro creado: {cilindro.dibujar()} con escalar {escalar}", limpiar=True)

    # ---------- opcion 2: mostrar figuras ----------
    def opcion2(self):
        self.escribir("Mostrando figuras...", limpiar=True)
        listaFiguras = self.servicio.listarFigurasActuales()
        if not listaFiguras:
            self.escribir("No hay figuras registradas")
            return
        for i, figuras in enumerate(listaFiguras, start=1):
            self.escribir(f"Figura: {i}, {figuras.getNombre()}")

    # ---------- opcion 3: figuras y sus valores ----------
    def opcion3(self):
        self.escribir("Mostrando figuras y sus valores: ", limpiar=True)
        listaFiguras = self.servicio.listarFigurasActuales()
        if not listaFiguras:
            self.escribir("No hay figuras registradas")
            return
        for i, figuras in enumerate(listaFiguras, start=1):
            self.escribir(
                f"Figura: {i}, {figuras.getNombre()}, Dibujo: {figuras.dibujar()}, "
                f"Volumen: {figuras.calcularVolumen():.2f}, "
                f"Area superficial: {figuras.getAreaSuperficial():.2f}"
            )

    # ---------- opcion 4: salir ----------
    def opcion4(self):
        self.ventana.destroy()


if __name__ == "__main__":
    ventana = tk.Tk()
    main(ventana)
    ventana.mainloop()