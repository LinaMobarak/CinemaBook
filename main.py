class movie:
    time = 2
    LstOfMovies = {"movie1":["a","ali","jack",8.5],"movie2":["b","ali","jack",9],
                   "movie3":["c","ahmed","katrina",4],"movie4":["d","ali","jack",8]}

    cinema1 = [1,30,0,{"movie1":10,"movie2":1.5,
               "movie3":4,"movie4":5}]

    cinema2 = [2,30,0,{"movie1":2.15,"movie2":2.15,
               "movie3":2,"movie4":2}]

    def __init__(self):
        pass

    def display(self,name):
        print(movie.LstOfMovies[name])

    def book(self,name,tickets):
        var1 = movie.cinema1[3]
        timee = var1[name]
        # print(var1)
        # print(timee)
        if (timee - movie.time)>0.15:
            var2 = movie.cinema2[3]
            timeee = var2[name]
            if (timeee - movie.time) > 0.15:
                print("Cancel")
            else:
                y = input("do you want to book : ")
                if y =='no':
                    print('cancel')
                else:
                    if movie.cinema2[1]<tickets and movie.cinema2[1]>0:
                        print("There is no available seats ,the number of seats that is available ",movie.cinema2[1])
                        x=input("do you want to book : ")
                        if x == 'yes':
                            movie.cinema2[1]-=tickets
                            movie.cinema2[2]+=tickets
                            print( "The id of the theater : ",movie.cinema2[0])
                        else :
                            print('Cancel ')

                    elif movie.cinema2[1]>=tickets:
                        movie.cinema2[1] -= tickets
                        movie.cinema2[2] += tickets
                        print("The id of the theater :",movie.cinema2[0])

                    else:
                        print('Cancel ')

        else:
            if movie.cinema1[1] < tickets and movie.cinema1[1]>0:
                print("There is no available seats ,the number of seats that is available ", movie.cinema2[1])
                x = input("do you want to book : ")
                if x == 'yes':
                    movie.cinema1[1] -= tickets
                    movie.cinema1[2] += tickets
                    print("The id of the theater :",movie.cinema1[0])
                else:
                    print('Cancel ')

            elif movie.cinema1[1] >= tickets:
                movie.cinema1[1] -= tickets
                movie.cinema1[2] += tickets
                print("The id of the theater :",movie.cinema1[0])

            else:
                print('Cancel ')





x = input("what is the name of the movie ? ")
y = int(input("what is the number of seats do you want : "))
p1 = movie()
p1.display(x)
x = input("Do you like the movie ?")
if x == 'yes':
    p1.book(x,y)
else:
    print("Thank you")

