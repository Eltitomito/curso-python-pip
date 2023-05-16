import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv('data.csv')
    print("Total de registros en el archivo CSV:", len(data))

    data = list(filter(lambda i: i['Continent'] == 'South America', data))
    print("Registros filtrados para Sudamérica:", len(data))

    country = input('Ingrese el país -> ')
    print("País ingresado:", country)

    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(country, countries, percentages)
    print("Gráfico de pie generado exitosamente.")

    result = utils.population_by_country(data, country)
    print(result)

    if result:
        print("País encontrado en los datos.")
        country_dict = result[0]
        labels, values = utils.get_population(country_dict)
        charts.generate_bar_chart(labels, values)
        print("Gráfico de barras generado exitosamente.")
    else:
        print("País no encontrado en los datos.")

if __name__ == '__main__':
    run()