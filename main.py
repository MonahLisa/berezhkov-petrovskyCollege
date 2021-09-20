class Student():
    course = 3901
    group_name = "группа 3901"
    number_bilet = 0
    avg_grade = 0
    name = "Васильев"

    def addFio(self):
        self.mname = input("Введите имя: ")
        self.lname = input("Введите отчество: ")
        self.name = self.name+" "+self.mname+" "+self.lname
        print("Имя студента - "+self.name)

    def goToCollege(self):
        self.avg_grade += 1
        return self.avg_grade
    def upCourse(self):
        self.course += 1
        self.group_name = self.group_name[0:len(self.group_name)-1] + str(self.course % 10)
        return self.group_name



s = Student()
print(s.goToCollege())
print(s.goToCollege())
print(s.avg_grade)
print(s.name)
s.addFio()
print(s.name)
k = Student()
print(k.name)
print(s.upCourse())



'''
using System;
using System.Collections.Generic; 
using System.Text; 

namespace ConsoleApplication1
{
	public class Program
	{
		public static void Main()
		{ 
			
			
			Console.WriteLine("Лабораторная 3");
			Console.WriteLine("\nПервое задание");
			double x = 0.0, a = 0.0, y=0.0;
			string str; 
			Console.Write("Введите значение параметра х = "); 
			str = Console.ReadLine(); 
			x = Convert.ToDouble(str);
			Console.Write("Введите значение параметра a = "); 
			str = Console.ReadLine(); 
			a = Convert.ToDouble(str);
			
			if(x < -5){
				y = a * Math.Pow(x, 2);
			}
			else if((x >= -5)&(x < 1)){
				y = a * Math.Abs(x);
			}
			else if(x >= 1){
				y = 1 / (a - x);
			}
			Console.Write("\n\t\tРезультаты вычислений:\n y = {0:f3}\n", y);
			
			
			
			int month, year;
			Console.WriteLine("\nВторое задание");
			Console.Write("Введите месяц = "); 
			str = Console.ReadLine(); 
			month = Convert.ToInt32(str);
			Console.Write("Введите год = "); 
			str = Console.ReadLine(); 
			year = Convert.ToInt32(str);
			
			if((year % 400 == 0)||((year % 4 == 0)&(year % 100 != 0))){
				Console.WriteLine("Год високосный");
				year = 1;
				
			}
			else{
				Console.WriteLine("Год не високосный");
				year = 0;
			}
			
			
			if(month>7){
				if(month % 2 == 0){
					Console.WriteLine("В месяце 31 день");
				}
				else{
					Console.WriteLine("В месяце 30 дней");
				}
			}
			else{
				if((year == 1)&(month % 2 == 0)){
					if(month == 2){
					Console.WriteLine("В месяце 29 дней");
					}
					else{
						Console.WriteLine("В месяце 30 дней");
					}
				}
				else if((year == 0)&(month % 2 == 0)){
					if(month == 2){
					Console.WriteLine("В месяце 28 дней");
					}
					else{
						Console.WriteLine("В месяце 30 дней");
					}
				}
				else if(month % 2 != 0){
					Console.WriteLine("В месяце 31 день");
				}
				
				
			}
			
			double S, P, A, B, C, MAX;
			Console.WriteLine("\nТретье задание");
			Console.Write("Введите A = "); 
			str = Console.ReadLine(); 
			A = Convert.ToInt32(str);
			Console.Write("Введите B = "); 
			str = Console.ReadLine(); 
			B = Convert.ToInt32(str);
			Console.Write("Введите C = "); 
			str = Console.ReadLine(); 
			C = Convert.ToInt32(str);
			MAX = Math.Max(Math.Max(A, B), C);
			
			if((A+B > C)&(A+C>B)&(B+C>A)){
				P = (A+B+C)/2;
				S = Math.Sqrt(P*(P-A)*(P-B)*(P-C));
				if((A==B)&(B==C)){
					Console.WriteLine("Треугольник равносторонний, остроугольный");
				}
				else if(((A==B)&(B!=C))||((A==C)&(C!=B))||((B==C)&(C!=A))){
					Console.WriteLine("Треугольник равнобедренный, остроугольный");
				}
				else if(MAX){}
			}
			else{
				Console.WriteLine("Такого треугольника не существует");
			}
			
			
			/*
			
			
			Console.WriteLine("Третье задание");
			Console.Write("Введите значение параметра a = "); 
			str = Console.ReadLine(); 
			a = Convert.ToInt32(str);
			Console.Write("Введите значение параметра b = "); 
			str = Console.ReadLine(); 
			b = Convert.ToInt32(str);
			List<double> listOfCubes = new List<double>(){
			};
			for (int i = a; i < b; i++){
				if(i % 2 == 0){
					listOfCubes.Add(Math.Pow(i, stepen));
				}
			}
			for (int i = a; i < b; i++){
				Console.Write(listOfCubes[i]);
			}
						
			
			
			
			
			//y = Math.Sin(Math.PI / 2 * x); 
			//Console.Write("\n\t\tРезультаты вычислений:\n y={0} y={0:f4} z={1:E5}\n", y, y/g);*/
		}
	}
}

'''


