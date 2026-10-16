from product import  add_product,update_product,view_products,delete_product,low_stock_alert
def main():
    while True:
        print("******welcome******")
        print("Enter Your choice")
        print("1.View Products")
        print("2.add products")
        print("3.Update products")
        print("4.Delete product")
        print("5.Low stock alerts")
        print("6.To exit")
        
        print("*****Thank you******")
        
        try :
            
            choice=int(input("Enter your choice")) 
            print("you entered",choice)
            
            
            if choice==1:
                view_products()
            
            elif choice==2:
                add_product()
            elif choice==3:
                update_product()
            elif choice==4:
                delete_product()
            elif choice==5:
                low_stock_alert()
            elif choice==6:
                print("Exiting")
                break
            else:
                print("Enter valid choice")
        except Exception as e:
            print("ERROR", e)
            
            
if __name__=="__main__":
    main()