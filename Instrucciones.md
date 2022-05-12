# CALCULADORA SALUDABLE
Elaborado por Ernesto Delgadillo
## Objetivo
Aplicar los conceptos vistos en las semanas 1 y 2, incluyendo el método IDEAL con el fin de solucionar el reto de la semana utilizando funciones, parámetros y tipos de datos.
## Contexto
Estar en forma se ha vuelto en un aspecto muy importante y cotidiano en nuestra sociedad hasta convertirse en un estilo de vida. Un aspecto importante para las personas que siguen este estilo de vida son los diferentes indicadores de su estado físico. (Peso, grasa, calorías, entre otros). Por eso en este reto vamos a implementar algunas más utilizadas por la "gente fitness".

## 1. Identificación del problema
Las personas necesitan saber si su peso se encuentra entre los indicadores del peso ideal, su porcentaje de grasa corporal, su índice metabólico basal y sus calorías quemadas realizando cierto tipo de ejercicios.
## 2. Definición del problema
**Información que conozco:**  
+ Fórmula **peso ideal**: *Hombre* = 56.2 + 1.41*(altura(cm)/2.54-60) y *Mujer* = 53.1 + 1.36 * (altura(cm)/2.54-60)
+ Fórmula **calorías quemadas**: (Tiempo de actividad (min) * MET * Peso(kg)) / 200
+ **Valores del MET**: --*Caminar*= 2  --*Tennis*= 5 --*Montar en biciclera*= 14 --*Correr*= 6 --*Nadar*= 9.8
+ Fórmula **indice de masa corporal (IMC)**= Peso(kg)/altura2(m)
+ Fórmula **porcentaje de grasa corporal**: --*Hombres adultos*= 1.20 * IMC + 0.23 * edad - 16.2
  > --*Mujeres adultas*= 1.20 * IMC + 0.23 * edad - 5.24
+ Fórmula **indice metabólico basal(calorías)**: *Hombres*=(13.397 * peso(kg)) + (4.799 * edad) - (5.677 * altura(cm)) + 88.362
  >--*Mujeres*= (9.247 * peso(kg)) + (3.098 * edad) - (4.330 * altura(cm)) + 447.593
  
**Información que debo conocer:**  
+ edad.
+ peso.
+ altura.
+ Si es hombre o mujer.
+ Que tipo de ejercicio realiza(Caminar, nadar, correr, Montar en bicicleta o jugar tenis).

**Dividir el problema en subproblemas:**
+ Solicitar si es hombre o mujer.
+ Solicitar edad.
+ Solicitar peso.
+ Solicitar altura.
+ Calcular el peso ideal (IMC).
+ Calcular calorias quedadas según el tipo de ejercicio.
+ Calcular el porcentaje de grasa corporal.
+ Calcular el índice metabólico basal.
## 3. Estrategia de solución
1. Leer los datos solicitados: -edad, -peso, -altura, -si es hombre o mujer.
2. Realizar las operaciones básicas de acuerdo con cada métrica utilizada, con el fin de saber el "*peso ideal*", las "*calorias quemadas*", el "*procentaje de grasa corporal*" y el "*índice metabólico basal*" de cada persona.

**Ejemplo:**  
--BIENVENIDO A SU CALCULADORA SALUDABLE--  
**Que operación deseas realizar:**
1. Conocer su peso ideal.
2. Conocer cantidad de calorias quemadas.
3. Conocer su porcentaje de grasa corporal.
4. Conocer su índice metabólico basal.
5. Salir
-----------------------------------------
4. **Conocer su índice metabólico basal.**  
Ingrese su edad(años): 18  
Ingrese su peso(kg): 60  
Ingrese su altura(cm): 157  
Eres hombre o Mujer?: Hombre
------------------------------------------
Su indice metabólico basal es: **123.275 calorías**  
Porfavor digite:
6. para retornar al menú anterior.
7. para salir.
## Conclusión
Gracias al método **IDEAL** podemos solucionar problemas de todo tipo, desde el más fácil hasta el más complejo de los problemas, ayudándonos a sistematizar y organizar nuestra solución u objetivos propuestos.