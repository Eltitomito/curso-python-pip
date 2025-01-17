import matplotlib.pyplot as plt

def generate_bar_chart(name,labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./bar_imgs/{name}.png')
  plt.close()

def generate_pie_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels, startangle=90, labeldistance=1.1, autopct='%1.1f%%', pctdistance=0.9)
  ax.axis('equal')
  plt.savefig(f'./pie_imgs/{name}.png')
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [100, 200, 300]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)


