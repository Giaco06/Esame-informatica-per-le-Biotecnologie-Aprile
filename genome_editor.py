class GenomeEditor:
    """
    Classe per l'editing di sequenze genomiche.
    Implementa la logica di inserimento singolo (ultima occorrenza) e multiplo,
    oltre all'annullamento di queste ultime operazioni.
    """
    def __init__(self) -> None:
        self.basi: str = 'ACGT'

    def edit_singolo(self, genome: str, insertion: str, insertion_point: str) -> str:
        """
        Inserisce una sequenza (insertion) subito dopo uno specifico target (insertion_point).
        Se il target compare più volte, la modifica avviene solo sull'ultima occorrenza.
        """
        last_insertion_point: int = genome.rfind(insertion_point)
        if last_insertion_point == -1:
            return genome

        restriction_site: int = last_insertion_point + len(insertion_point)
        edited_genome: str = genome[:restriction_site] + insertion + genome[restriction_site:]
        return edited_genome

    def edit_multiplo(self, genome: str, insertions: list[str], insertion_points: list[str]) -> str:
        """
        Esegue modifiche in sequenza. Se insertion appare m <= k volte, viene
        replicata m volte durante l'inserimento.
        """
        current_genome = genome
        conteggio_repliche: dict[str, int] = {}

        for i in range(len(insertions)):
            ins: str = insertions[i]
            ins_point: str = insertion_points[i]

            if ins in conteggio_repliche:
                conteggio_repliche[ins] += 1
            else:
                conteggio_repliche[ins] = 1

            m: int = conteggio_repliche[ins]
            actual_insertion: str = ins * m
            current_genome = self.edit_singolo(current_genome, actual_insertion, ins_point)

        return current_genome

    def del_edit(self, genome: str, insertion_point: str, insertion: str) -> str:
        """
        Annulla un singolo edit rimuovendo la sequenza 'insertion' subito dopo
        l'ultima occorrenza di 'insertion_point'.
        """
        last_insertion_point: int = genome.rfind(insertion_point)

        if last_insertion_point == -1:
            return genome

        start_insertion: int = last_insertion_point + len(insertion_point)
        end_insertion: int = start_insertion + len(insertion)

        if genome[start_insertion:end_insertion] == insertion:
            undone_genome: str = genome[:start_insertion] + genome[end_insertion:]
            return undone_genome

        return genome

    def del_edit_multiplo(self, genome: str, insertion_points: list[str], insertions: list[str]) -> str:
        """
        Annulla una sequenza di k edit. Applica la regola delle repliche (m volte).
        Se un'operazione non è valida, il processo si interrompe immediatamente.
        """
        current_genome: str = genome
        conteggio_repliche: dict[str, int] = {}

        for i in range(len(insertions)):
            ins: str = insertions[i]
            ins_point: str = insertion_points[i]

            if ins in conteggio_repliche:
                conteggio_repliche[ins] += 1
            else:
                conteggio_repliche[ins] = 1

            m: int = conteggio_repliche[ins]
            actual_insertion: str = ins * m

            genome_pre_rimozione: str = current_genome
            current_genome = self.del_edit(current_genome, ins_point, actual_insertion)

            if current_genome == genome_pre_rimozione:
                print(f"  [!] Interruzione: impossibile rimuovere '{actual_insertion}' dopo '{ins_point}'.")
                break

        return current_genome