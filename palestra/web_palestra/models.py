from django.db import models

class Utenti(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    data_nascita = models.DateField()
    indirizzo = models.CharField(max_length=255)
    emailIndex = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    foto = models.TextField()
    usernameIndex = models.CharField(max_length=50)
    password_utente = models.CharField(max_length=255)
    data_registrazione = models.DateField()

    def __str__(self):
        return f'{self.nome} {self.cognome}'

class Insegnanti(models.Model): 
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    data_nascita = models.DateField()

    def __str__(self):
        return f'{self.nome} {self.cognome}'

class Discipline(models.Model): 
    nome = models.CharField(max_length=100)
    descrizione = models.TextField()
    insegnante = models.ForeignKey(Insegnanti, on_delete=models.CASCADE)
    prezzo_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Incontri(models.Model): 
    id = models.AutoField(primary_key=True)
    fk_id_disciplinaIndex = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    fk_id_insegnanteIndex = models.ForeignKey(Insegnanti, on_delete=models.CASCADE)

    def __str__(self):
        return f"Incontro di {self.fk_id_disciplinaIndex.nome} con {self.fk_id_insegnanteIndex.nome}"

class Calendario(models.Model): 
    data_incontro = models.DateField()
    ora_inizio_incontro = models.TimeField()
    ora_fine_incontro = models.TimeField()
    incontro = models.ForeignKey(Incontri, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.data_incontro} dalle {self.ora_inizio_incontro} alle {self.ora_fine_incontro}'

class Abbonamenti(models.Model): 
    utenti = models.ForeignKey(Utenti, on_delete=models.CASCADE,db_column='fk_id_utente')
    incontro = models.ForeignKey(Incontri, on_delete=models.CASCADE,db_column='fk_id_incontro')
    sedute = models.IntegerField()
    stato_pagamento = models.CharField(max_length=255)
    costo_totale = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Abbonamento di {self.utenti.nome} {self.utenti.cognome}'

class AbbonamentiIncontri(models.Model): 
    fk_id_abbonamento = models.ForeignKey(Abbonamenti, on_delete=models.CASCADE,db_column='fk_id_abbonamento')
    fk_id_incontro = models.ForeignKey(Incontri, on_delete=models.CASCADE,db_column='fk_id_incontro')

    class Meta:
        db_table = 'abbonamenti_incontri'  # Specifica il nome della tabella esistente
        managed = False 

    def __str__(self):
        return f"Abbonamento: {self.fk_id_abbonamento}, Incontro: {self.fk_id_incontro}"