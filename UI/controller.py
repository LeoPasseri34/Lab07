import flet as ft

from UI.view import View
from model.modello import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # other attributes
        self._mese = 0

    def handle_umidita_media(self, e):
        mese = self._view.dd_mese.value
        if (mese==""):
            self._view.create_alert("Attenzione, selezionare un mese!")
            self._view.update_page()
            return
        else:
            stats_umidita = self._model.get_umidita_media(mese)
            for r in stats_umidita:
                localita = r["Localita"]
                media = round(r["umidita_media"], 4)  # Arrotonda a 4 cifre decimali
                self._view.lst_result.controls.append(ft.Text(f"{localita}: {media}"))
                self._view.update_page()


    def handle_sequenza(self, e):
        mese = self._view.dd_mese.value
        if mese == "":
            self._view.create_alert("Attenzione, selezionare un mese!")
            return
        sequenza, costo = self._model.calcola_sequenza(mese)
        print(sequenza)
        self._view.lst_result.controls.clear()
        self._view.lst_result.controls.append(ft.Text(f"Il costo della sequenza è {costo}"))
        for i in sequenza:
            self._view.lst_result.controls.append(ft.Text(i))
        self._view.update_page()

    def read_mese(self, e):
        self._mese = int(e.control.value)


