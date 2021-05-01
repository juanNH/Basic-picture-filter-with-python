import cv2
import numpy as np
#la funcion vacio no hace nada
def vacio():
    pass
 #define la convultion kernels
identificador =np.array([[0,0,0],[0,1,0],[0,0,0]])
sharpen = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])

gaussian_kernel1 = cv2.getGaussianKernel(3,0)
gaussian_kernel2= cv2.getGaussianKernel(5,0)
box_kernel = np.array([[1,1,1],[1,1,1],[1,1,1]],np.float32)/9.0
kernels = [identificador, sharpen,gaussian_kernel1,gaussian_kernel2,box_kernel]
# lee la imagen y crea una copia en gris
color_or=cv2.imread("test.png") 
gris_or=cv2.cvtColor(color_or,cv2.COLOR_BGR2GRAY)
#crea la interfaz 
# crea la ventana
cv2.namedWindow("app")
# barra de contraste, brillo, filtro, imagen gris
cv2.createTrackbar("contraste","app",1,100,vacio)
cv2.createTrackbar("brillo","app",50,100,vacio)
cv2.createTrackbar("filtro","app",0,len(kernels)-1,vacio)
cv2.createTrackbar("gris","app",0,1,vacio)
#loop de la ventana
contador = 1
while True:   
    #muestra todas las barras
    esc_gris = cv2.getTrackbarPos("gris","app")
    contraste = cv2.getTrackbarPos("contraste","app")
    brillo= cv2.getTrackbarPos("brillo","app")
    kernel_idx =cv2.getTrackbarPos('filtro',"app")
    #aplica el filtro
    modificador_color = cv2.filter2D(color_or,-1,kernels[kernel_idx])
    modificador_gris = cv2.filter2D(gris_or,-1,kernels[kernel_idx])
    
    #aplica el brillo y contraste
    modificador_color = cv2.addWeighted(modificador_color, contraste, np.zeros_like(color_or),0,brillo-50)
    modificador_gris = cv2.addWeighted(modificador_gris, contraste, np.zeros_like(gris_or),0,brillo-50)
    # espera para cerrarse despues de precionar la tecla
    key = cv2.waitKey(100)
    if key == ord("q"):
        break
    elif key == ord("s"):
        #guardar la imagen
        if esc_gris == 0:
            cv2.imwrite("output-[].png".format(contador), modificador_color)
        else:
            cv2.imwrite("output-[].png".format(contador), modificador_gris)
        contador += 1
        
        
    
    if esc_gris == 0:
        cv2.imshow("app",modificador_color)
    else:
        cv2.imshow("app",modificador_gris)
cv2.destroyAllWindows()