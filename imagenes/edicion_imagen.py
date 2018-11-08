#ALGORITMOS FUNDAMENTALES
#AUTOR: STALIN MAZA
#VERSION 2.3
#TRATAMIENTO DE IMAGENES EN PYTHON - edicion_imagen.py
#2016-Ene-09
#DOCENTE: Ing. Iván Grijalva

#MODULO DE LIBRERIAS
from scipy import misc
from scipy import *
import numpy as np # funciones numéricas (arrays, matrices, etc.)
import matplotlib.pyplot as plt # funciones para representación gráfica
import matplotlib.image as mpimg
from PIL import Image
import pylab as p

#NOTAS
#Se uso Winpython Portable ya que viene con todas las librerias incorporadas
#Link de Descarga: https://sourceforge.net/projects/winpython/

#FUNCIONES
def grisI(): #IMAGEN GRIS
    img = 'mario.png' #asignamos la direccion de la imagen a una variable    
    image = Image.open(img).convert("L") #abrimos la imagen y la convertimos
    #abrimos la imagen y la convertimos a una de tipo PIL Image(Monocromatico)
    array = np.asarray(image) #creamos un array numpy de la imagen   
    tamanio = image.size #alto y ancho  
    plt.imshow(array, cmap='gray') #imagen con ejes y a escala de grises
    print("Imagen Gris")
    plt.show() #mostramos la imagen

def mostrarI():    
    face = misc.face() #creamos un array numpy de la imagen face 
    plt.imshow(face) #mandamos el array a imprimir
    plt.show() #mostramos la impresion

def monocromaticaI():  #IMAGEN MONOCROMATICA
    img = mpimg.imread('mario.png' ) #leemos la imagen y guardamos en un array
    lum_img = img[:,:,1] #crea un array del primer panel imagen 
    imgplot = plt.imshow(lum_img) #mando a imprimir el primer panel de la imagen    
    print("Imagen Monocromatica")
    plt.show()

def sombraB(): #CAMBIAR SOMBRA IMAGEN
    def sombrear(img, porcentaje):
        #img guarda la imagen que sera modificada
        #porcentaje: guarda el  valor entre 0(sin_cambios)-1(blanco_total)
        img_color = img + (np.ones(img.shape) - img) * porcentaje
        #creamos otro array lleno de ceros que sus valores se multiplican por el valor
        #del procentaje a sombrear en blanco y se suma a los valores de la imagen original
        return img_color #retornamos la imagen
    
    foto = mpimg.imread('molino.png') #leemos la imagen
    foto_mod = sombrear(foto, 0.7) #llamamos a sombrear con la imagen y el porcentaje
    plt.imshow(foto_mod)  #mandamos a imprimir la foto(array)  
    print("Imagen Sombreada en Blanco")
    plt.show() #mostramos la imagen

def sombraN(): #CAMBIAR SOMBRA IMAGEN
    def sombrear(img, porcentaje):
        #img guarda la imagen que sera modificada
        #porcentaje: guarda el  valor entre 0(sin_cambios)-1(negro_total)
        img_color = img * (1 - porcentaje)
        return img_color
    
    foto = mpimg.imread('molino.png') #leemos la imagen
    print(foto.shape)
    foto_mod= sombrear(foto, 0.5) #sombreamos la imagen
    plt.imshow(foto_mod)  #mandamos a imprimir la foto(array) 
    print("Imagen Sombreada en Negro")
    plt.show() #mostramos la imagen
    
def f6():   
    windmills = mpimg.imread('molino.png')
    def shade(imag, percent):
        """
        imag: the image which will be shaded
        percent: a value between 0 (image will remain unchanged
             and 1 (image will be blackened)
        """
        tinted_imag = imag * (1 - percent)
        return tinted_imag
    
    def vertical_gradient_line(image, reverse=False):    
        #We create a horizontal gradient line with the shape (1, image.shape[1], 3))
        #The values are incremented from 0 to 1, if reverse is False,
        #otherwise the values are decremented from 1 to 0."""
    
        number_of_columns = image.shape[1]
        if reverse:
            C = np.linspace(1, 0, number_of_columns)
        else:
            C = np.linspace(0, 1, number_of_columns)
        C = np.dstack((C, C, C))
        return C
    horizontal_brush = vertical_gradient_line(windmills,reverse=True)
    tinted_windmills =  windmills * horizontal_brush
    plt.axis("off")
    plt.imshow(tinted_windmills)
    #plt.show()

def f7():
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    img = mpimg.imread('molino.png')
    print(img,len(img))
    def vertical_gradient_line(image, reverse=False):
        """
        We create a horizontal gradient line with the shape (1, image.shape[1], 3))
        The values are incremented from 0 to 1, if reverse is False,
        otherwise the values are decremented from 1 to 0.
        """
        number_of_columns = image.shape[1]
        if reverse:
            C = np.linspace(1, 0, number_of_columns)
        else:
            C = np.linspace(0, 1, number_of_columns)
            C = np.dstack((C, C, C))
        return C
    horizontal = vertical_gradient_line(img)
    print(horizontal,len(horizontal))
    #tinted_windmills =  windmills * horizontal
    #plt.axis("off")
    #plt.imshow(tinted_windmills)
    #plt.show()
    
def subploters():   
    charlie = mpimg.imread('mario.png')
    #  colormaps plt.cm.datad
    cmaps = set(plt.cm.datad.keys())
    x = [  (4,3,1, (1, 0, 0)), (4,3,2, (0.5, 0.5, 0)), (4,3,3, (0, 1, 0)), 
           (4,3,4, (0, 0.5, 0.5)),  (4,3,(5,8), (0, 0, 1)), (4,3,6, (1, 1, 0)), 
           (4,3,7, (0.5, 1, 0) ),               (4,3,9, (0, 0.5, 0.5)),
           (4,3,10, (0, 0.5, 1)), (4,3,11, (0, 1, 1)),    (4,3,12, (0.5, 1, 1))]    
    fig = plt.figure(figsize=(6, 5))
    #fig.subplots_adjust(bottom=0, left=0, top = 0.975, right=1)
    for nrows, ncols, plot_number, factor in x:
        sub = fig.add_subplot(nrows, ncols, plot_number)
        sub.set_xticks([])
        plt.colors()        
        sub.imshow(charlie*0.0002, cmap=cmaps.pop())
        sub.set_yticks([])
    fig.show()
    
def rotarI():
    img = mpimg.imread('linux.png' ) #abrimos la imagen
    print("Vamos a rotar la imagen")
    ang = int(input("Ingrese 1 izquierda,2 inversa y 3 derecha\n"))
    rotar = np.rot90(img,ang) #rotamos imagen 1-izquierda ,2-inversa°,3-derecha  
    plt.axis('off') #ocultamos los ejes
    plt.imshow(rotar) #mandamos a imprimir la imagen
    print("Imagen Rotada") #mostramos la imagen
    plt.show()
    
def reducirI():    
    imagen = Image.open("mario.png") #abrimos la imagen 
    reducida = imagen.resize((400, 300)) #Obtenemos la imagen del tamaño indicado
    reducida.show() #mostramos la imagen    
    #reducida.save("reducida.png") #guardamos la imagen

def girarI():
    imagen = Image.open("mario.png")  #abrimos la imagen
    ang = int(input("Ingrese el angulo a girar:\n")) #ingresamos el angulo a girar    
    rotar = imagen.rotate(ang)# guardamos la imagen girada
    rotar.show() #mostramos la imagen
    #rotar.save("girada.png") #guardamos la imagen
    
def unir():
    def mayor(a,b):
        if a > b:
            return a
        else:
            return b        
    
    imagen1 = Image.open("nevar1.jpg")
    imagen2 = Image.open("nevar2.jpg")
    ancho1,alto1 = imagen1.size[0],imagen1.size[1]
    ancho2,alto2 = imagen2.size[0],imagen2.size[1]
    a,b = mayor(ancho1,ancho2), mayor(alto1,alto2)
    print(ancho2,alto2)   
    final = Image.new("RGB",(a*2,b),"black")
    final.paste(imagen1, (0,0))
    final.paste(imagen2, (a,0))
    final.show()
    print("Imagenes Unidas Correctamente")
    #final.save("unida.jpg")

def miniaturaI():
    imagen = Image.open("mario.png") #uardamos la imagen
    miniatura = (160, 120) #damos el tamaño a la miniatura
    imagen.thumbnail(miniatura) #con la funcion thumbnail creamos la miniatura de las medidas dadas
    imagen.show() #mostramos la imagen
    #imagen.save("miniatura.jpg") #guardamos la imagen
    
def variasI():
    def colocar(img, n, m=1):
        #La Imagen "img" va a ser repetida n veces in 
        #posicion vertical and m veces en posicion horizontal.    
        if n == 1:
            cuadro = img
        else:
            endI = []
            for i in range(n):
                endI.append(img)  
            cuadro = np.concatenate(endI, axis=1 )
        if m > 1:
            endI = []
            for i in range(m):
                endI.append(cuadro)  
            cuadro = np.concatenate(endI, axis=0 )          
        return cuadro
    
    imagen = mpimg.imread('mario.png') #leemos la imagen y guardamos en un arreglo
    duplicada = colocar(imagen, 4, 4)#colocamos la imagen y ponemos numero filas,columnas a imprimir
    plt.imshow(duplicada) #mandamos a imprimir la imagen
    print("Imprimimos varias imagenes en un solo cuadro")
    plt.show() #mostramos la imagen

def eleccion():
    print("---------------------SALIDA---------------")
    seleccion = int(input("Ingrese su seleccion: \n"))
    if seleccion == 1:
        grisI()
    elif seleccion == 2:
        reducirI()
    elif seleccion == 3:
        girarI()
    elif seleccion == 4:
        rotarI()
    elif seleccion == 5:
        mostrarI()
    elif seleccion == 6:
        sombraB()
    elif seleccion == 7:
        sombraN()
    elif seleccion == 8:
        monocromaticaI()
    elif seleccion == 9:
        miniaturaI() 
    elif seleccion == 10:
        unir()
    elif seleccion == 11:
        variasI()
    elif seleccion == 12:
        subploters()
    else:
        print("Seleccion no corresponde al programa")
    salir()
    
def salir():
    volver = input("Desea Volver al Menu Y/N: \n")
    if volver == "Y" or volver == "y":
        main()
    else:
        print("Programa Terminado")
    
def menu():
    print("---------------------MENU---------------")
    print("\tBienvenidos al Programa Stalin")
    print("Aprenderemos tratamiento de imagenes con Numpy-Matplotlib-Spicy\n")
    print("1. Imagen a escala de Grises")
    print("2. Reducir tamaño de una Imagen")
    print("3. Girar Imagen(Primera Forma)")
    print("4. Girar Imagen(Segunda Forma)")
    print("5. Mostrar Imagen)")
    print("6. Imagen Sombreado Blanco")
    print("7. Imagen Sombreado Negro")
    print("8. Imagen Monocromatica)")
    print("9. Miniatura de una Imagen")
    print("10. Unir dos Imagenes")
    print("11. Imprimir Varias Imagenes")
    print("12. Subploters de Imagenes")

def main():
    menu()
    eleccion()

main()
#f6() #no me corre, el codigo no me sirve
#f7() #no vale, el codigo no me corre
