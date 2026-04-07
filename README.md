# Esame-informatica-per-le-Biotecnologie-Aprile
#Progetto: Simulatore di Genome Editing

Prodotto da Campi e Watson


## Descrizione del Progetto
Questo progetto implementa un simulatore software scritto in Python per simulare operazioni avanzate di editing genomico. Il sistema permette di alterare una sequenza di DNA di partenza (genoma) inserendo o rimuovendo specifiche sequenze (`insertions`) in corrispondenza di precisi siti bersaglio (`insertion points`).

---

## Moduli e Funzionalità Implementate
La classe `GenomeEditor` offre quattro metodi principali:

### 1. Inserimento Singolo (`edit_singolo`)
Metodo che esegue un singolo inserimento nel genoma.
* **Regola dell'Ultima Occorrenza:** Se il genoma presenta molteplici `insertion points` identici, l'algoritmo (sfruttando la ricerca *reverse*) garantisce che la modifica avvenga **solo ed esclusivamente sull'ultimo** target individuato. Se il target non è presente, il genoma non subisce alterazioni.

### 2. Inserimento Multiplo con Repliche (`edit_multiplo`)
Metodo che applica una sequenza di `k` modifiche in cascata, ricevendo in input le liste degli inserti e dei target.
* **Regola delle Repliche (m <= k):** Il sistema tiene traccia di quante volte una specifica `insertion` viene richiesta. Alla m-esima occorrenza di una data stringa nella lista, l'algoritmo replica l'inserimento m volte consecutive.

### 3. Annullamento Singolo (`del_edit`)
Metodo progettato per effettuare la rimozione di una specifica modifica.
* **Rimozione di Sicurezza Condizionata:** La funzione individua l'ultimo `insertion point` e verifica tramite *slicing* se la sequenza immediatamente successiva corrisponde in modo esatto all'`insertion` richiesta. L'operazione rimuove una singola occorrenza per chiamata.

### 4. Annullamento Multiplo (`del_edit_multiplo`)
Metodo che tenta di annullare una catena di `k` modifiche, gestendo sia le repliche che i potenziali errori di sequenza.
* **Gestione Repliche Inversa:** Utilizza la stessa logica matematica del metodo di inserimento. Alla m-esima occorrenza, il sistema cercherà di rimuovere un blocco replicato m volte.
* **Interruzione Automatica:** Se un'operazione di rimozione fallisce, il ciclo rileva l'invarianza della stringa genomica e interrompe istantaneamente l'esecuzione (`break`), restituendo il genoma ripristinato fino all'ultimo step valido.
