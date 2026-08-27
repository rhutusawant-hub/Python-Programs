#1) * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# ----->
# n = int(input("Enter length of triangle : "))
# for i in range(n):
#     for j in range(i + 1):
#         print("* ",end = "")
#     print()




#2) * * * * * 
# * * * * 
# * * * 
# * * 
# *
#  ------->
# n = int(input("Enter length of triangle : "))
# for i in range(n):
#     for j in range( n-i ):
#         print("*",end = " ")
#     print()





#3)         * 
#         * * 
#       * * * 
#     * * * * 
#   * * * * * 
# ------------>
# n = int(input("Enter length of triangle : "))
# for i in range(n):
#     for j in range( n-i ):
#         print(" ",end = " ")
#     for k in range(i + 1):
#         print("* ",end = "")
#     print()




#4) *****
22
#    ****
#     ***
#      **
#       *
# ------->
# n = int(input("Enter length of triangle : "))
# for i in range(n):
   
#     for j in range(i + 1):
#         print(" ",end = "")
#     for k in range(n-i):
#         print("*",end = "")
#     print()





#5)   * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 
# ----------->
# n = int(input("Enter length of triangle: "))                          
# for i in range(1, n+1):
#     for j in range(n-i):
#         print(" " , end = "")                                             
#     for k in range(i):
#         print("* ", end ="")
#     print() 
    
    
    
#6)   *
#    ***
#   *****
#  *******
# *********
#------->
# n = int(input("Enter length of triangle: "))
# for i in range(1, n+1):
#     for j in range(n-i):
#         print(" " , end = "")
#     for k in range(2*i - 1):
#         print("*", end ="")
#     print() 