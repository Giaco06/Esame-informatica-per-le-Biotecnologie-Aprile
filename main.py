from genome_editor import GenomeEditor

def main() -> None:
    editor = GenomeEditor()
    print(" ––– SIMULATORE DI GENOME EDITING –––\n")

    # ---------------------------------
    # TEST 1: edit singolo
    # ---------------------------------
    print("1. TEST 1: edit singolo")
    genoma_test: str = "AAATCGCGCGTCATAGTCGGA"
    insertion_point: str = 'TC'
    insertion: str = '[INS_1]'

    risultato_singolo: str = editor.edit_singolo(genoma_test, insertion, insertion_point)
    print(f"Genoma originale: {genoma_test}")
    print(f"Punto di inserimento: {insertion_point}")
    print(f"Genoma modificato: {risultato_singolo}\n")

    # ----------------------------------
    # TEST 2: edit multiplo
    # ----------------------------------
    print("2. TEST 2: edit multiplo")
    genoma_base_multipolo: str = 'ACTGAAATGCCCCTGAAA'
    insertion_points: list[str] = ['TG', 'AA', 'CC', 'TG']
    insertions: list[str]       = ['[INS_1]', '[INS_2]', '[INS_1]', '[INS_1]']

    risultato_mulitiplo: str = editor.edit_multiplo(genoma_base_multipolo, insertions, insertion_points)
    print(f"Genoma originale: {genoma_base_multipolo}")
    print(f"Genoma finale: {risultato_mulitiplo}\n")

    # -----------------------------------
    # Test 3: singola delezione
    # -----------------------------------
    print("3. TEST 3: singola delezione")
    genoma_editato: str = "AAATCGCGCGTCATAGTC[INS_1]GGA"

    risultato_undo: str = editor.del_edit(genoma_editato, 'TC', '[MAGIC]')
    print(f"Genoma editato: {genoma_editato}")
    print(f"Operazione: Rimuovi '[INS_1]' dopo l'ultimo 'TC'")
    print(f"Genoma annullato: {risultato_undo}\n")

    # ----------------------------------------
    # TEST 4: delezione multipla con repliche
    # ----------------------------------------
    print("4. TEST 4: delezione multipla con repliche")
    # CORRETTO: aggiunto l'uguale
    genoma_edit_multipli: str = "ACTGAAATGCCCC[INS_1][INS_1]TG[INS_1][INS_1][INS_1][INS_1]AAA[INS_2]"

    del_points: list[str] = ['TG', 'CC', 'XX']
    del_ins: list[str]    = ['[INS_1]', '[INS_1]', '[INS_2]']

    print(f"Genoma di partenza: {genoma_edit_multipli}")
    print("Tentativo di rimozione in sequenza:")
    print("  1. '[INS_1]' dopo 'TG' (1 replica)")
    print("  2. '[INS_1]' dopo 'CC' (2 repliche)")
    print("  3. '[INS_2]' dopo 'XX' (1 replica -> Fallirà e bloccherà tutto)")

    risultato_del_multiplo: str = editor.del_edit_multiplo(genoma_edit_multipli, del_points, del_ins)
    print(f"Genoma finale:      {risultato_del_multiplo}\n")
