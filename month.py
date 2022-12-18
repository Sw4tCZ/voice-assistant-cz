from datetime import datetime
# definování měsíců v cz
months = ["Unknown",
          "Leden",
          "Únor",
          "Březen",
          "Duben",
          "Květen",
          "Červen",
          "Červenec",
          "Srpen",
          "Září",
          "Říjen",
          "Listopad",
          "Prosinec"]

now = (datetime.now())
month = (months[now.month])


