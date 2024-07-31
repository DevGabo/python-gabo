import matplotlib.pyplot as a

def generate_pie_chart():
    labels = ['A','B','C']
    values = [200,34, 120]

    #fig, ax = plt.subplot()
    #ax.pie(values,labels)
    #plt.savefig('pie.png')
    #plt.close()

    fig, ax = a.subplots()
    a.pie(values,labels=labels)
    a.savefig('pie.png')
    a.close()
    #pylot.show()