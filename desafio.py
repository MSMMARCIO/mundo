'''sabendo que a area de um triangulo é igual a base * altura / 2
 crie uma função que que receba a base e altura e retorne a area
 '''


    
   
def calcular_area_triangulo(base, altura):
    
    area = (base * altura) / 2
    return area

if __name__ == "__main__":
    

    
        base = float(input("Digite o valor da base do triângulo: "))
        altura = float(input("Digite o valor da altura do triângulo: "))
        area_resultado = calcular_area_triangulo(base, altura)
        print(f"A área do triângulo é {area_resultado:.2f} unidades quadradas.")
    
        
        
    
    

