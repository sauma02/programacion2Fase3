from servicios.ServicioCrearFigura import ServicioCrearFigura;
import time
class main:
    servicio = ServicioCrearFigura();
    flag = True;
    i= 0;
    while flag:
        
        print("Bienvenido al sistema de modelado de figuras 3d, porfavor seleccione una de las siguientes opciones")
        time.sleep(2)
        print("1- Crear una figura")
        print("2- Mostrar figuras registradas")
        print("3- Mostrar figuras y sus valores ")
        print("4- Salir")
        
        opcion = int(input("Ingrese una opcion del 1 al 4"))
        
        match opcion:
            case 1:
                flag2 = True
                while flag2:
                    print("¿Que figura desea crear?")
                    print("1- Esfera")
                    print("2- Cubo")
                    print("3- Cilindro")
                    print("4- Volver")
                    opcion2 = int(input("Seleccione solo valores del 1 al 4"))
                    match opcion2:
                        case 1:
                            radio = float(input("Ingrese el valor del radio."))
                            escalar = float(input("Ingrese el valor de la escala a la cual se hara el calculo de la figura"))
                            esfera = servicio.crearEsfera(radio, escalar);
                            time.sleep(2)
                            print(f"Esfera creada: {esfera.dibujar()} con escalar {escalar}");
                        case 2:
                            lado = float(input("Ingrese el valor de uno de los lados."))
                            escalar = float(input("Ingrese el valor de la escala a la cual se hara el calculo de la figura"))
                            cubo = servicio.crearCubo(lado, escalar);
                            time.sleep(2)
                            print(f"Esfera creada: {cubo.dibujar()} con escalar {escalar}");
                            
                        case 3:
                            radio = float(input("Ingrese el valor del radio."))
                            altura = float(input("Ingrese el valor de la altura."))
                            escalar = float(input("Ingrese el valor de la escala a la cual se hara el calculo de la figura"))
                            cilindro = servicio.crearCilindro(radio,altura,escalar);
                            time.sleep(2)
                            print(f"Esfera creada: {cilindro.dibujar()} con escalar {escalar}");
                        case 4:
                            print("Saliendo..")
                            time.sleep(2)
                            print("adios");
                            flag2 = False;
                        case _:
                            print("opcion invalida")
            case 2:
                print("mostrando figuras...")
                time.sleep(2);
                listaFiguras = servicio.listarFigurasActuales();
                for figuras in listaFiguras:
                    i =+ 1
                    print(f"Figura: {i}, {figuras.getNombre()}");
                flag = False;    
            case 3:
                print("Mostrando figuras y sus valores: ")
                time.sleep(2);
                listaFiguras = servicio.listarFigurasActuales();
                for figuras in listaFiguras:
                    i =+ 1;
                    print(f"Figura: {i}, {figuras.getNombre()}, Dibujo: {figuras.dibujar()}, Volumen: {figuras.calcularVolumen()}, Calcular area superficial: {figuras.getAreaSuperficial()}")
            case 4:
                print("Saliendo...");
                time.sleep(2);
                print("Adios.")
                flag = False;
            case _:
                print("Opcion no valida");           
                
                 
            
        
        
    
    