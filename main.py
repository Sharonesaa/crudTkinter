from tkinter import Tk, Label, LabelFrame, Button, Radiobutton, Entry, Toplevel, StringVar, ttk, CENTER, EW, E, N, W
from tkcalendar import DateEntry
from pymysql import Error, err, connect
from random import shuffle


class Menu():

    def __init__(self, root):

        # ventana principal
        self.root = root
        self.root.title('Juegos')
        self.root.geometry("400x450")
        self.root.resizable(0, 0)

        self.frame = LabelFrame(self.root, text='Menu', padx=15, pady=15, font=(100))
        self.frame.grid(row=0, column=0, padx=40, pady=40)

        self.message = Label(self.frame, text='', height=1, width=40)
        self.message.grid(row=1, column=0, sticky=N)

        Button(self.frame, text='REGISTER', command=self.registerWindow, height=3, width=25).grid(row=2, column=0)
        Button(self.frame, text='LOGIN', command=self.loginWindow, height=3, width=25).grid(row=3, column=0)
        Button(self.frame, text='TOP PLAYERS', command=self.topPlayersWindow, height=3, width=25).grid(row=4, column=0)
        Button(self.frame, text='EXIT', command=self.root.destroy, height=3, width=25).grid(row=5, column=0)
        Button(self.root, text='ADMIN', command=self.adminWindow).grid(padx=10, sticky=E)

    def registerWindow(self):

        self.rWindow = Toplevel()
        self.rWindow.title('Juegos / Register')
        self.rWindow.geometry("300x340")
        self.rWindow.resizable(0, 0)

        registerFrame = LabelFrame(self.rWindow, text='Register', padx=15, pady=15, font=(100))
        registerFrame.grid(row=0, column=0, padx=30, pady=40)

        Label(registerFrame, text='Player Name:', pady=5).grid(row=1, column=0, sticky=E)
        Label(registerFrame, text='Birthday:', pady=5).grid(row=2, column=0, sticky=E)
        Label(registerFrame, text='Sex:', pady=5).grid(row=3, column=0, sticky=E)
        Label(registerFrame, text='Email:', pady=5).grid(row=4, column=0, sticky=E)

        playerName = Entry(registerFrame)
        playerName.focus()
        playerName.grid(row=1, column=1, columnspan=2)

        birthday = DateEntry(registerFrame, date_pattern='yyyy-MM-dd')
        birthday.grid(row=2, column=1, columnspan=2, sticky=EW)

        sex = StringVar()
        Radiobutton(registerFrame, text='F', value='F', variable=sex, indicatoron=False).grid(row=3, column=1)
        Radiobutton(registerFrame, text='M', value='M', variable=sex, indicatoron=False).grid(row=3, column=2)

        email = Entry(registerFrame)
        email.grid(row=4, column=1, columnspan=2)

        Button(registerFrame, text='Save', command=lambda: self.register(playerName.get(), birthday.get(), sex.get(), email.get()), height=2, width=25).grid(row=5, column=0, columnspan=3, sticky=EW)
        Button(registerFrame, text='Back', command=self.rWindow.destroy, height=2, width=25).grid(row=6, column=0, columnspan=3, sticky=EW)

    def loginWindow(self):

        self.lgWindow = Toplevel()
        self.lgWindow.title('Juegos / Login')
        self.lgWindow.geometry("610x370")
        self.lgWindow.resizable(0, 0)

        self.lgFrame = LabelFrame(self.lgWindow, text='Login', padx=15, pady=15, font=(100))
        self.lgFrame.grid(row=0, column=0, padx=190, pady=70)
        self.lgMessage = Label(self.lgFrame, text='')
        self.lgMessage.grid(row=3, column=0, columnspan=3, sticky=EW, pady=10)

        Label(self.lgFrame, text='Player Name:', pady=5).grid(row=0, column=0, sticky=E)

        self.playerEntry = Entry(self.lgFrame)
        self.playerEntry.focus()
        self.playerEntry.grid(row=0, column=1, columnspan=2, pady=20)
        self.playerEntry.bind("<Return>", lambda e: self.loginWindow2(self.playerEntry.get()))

        Button(self.lgFrame, text='Entry', command=lambda: self.loginWindow2(self.playerEntry.get()), height=2).grid(row=1, column=0, columnspan=3, sticky=EW)
        Button(self.lgFrame, text='Back', command=self.lgWindow.destroy, height=2).grid(row=2, column=0, columnspan=3, sticky=EW)

    def loginWindow2(self, playerName):

        query = "SELECT * FROM player WHERE playerName = %s"
        result = self.runQuery(query, (playerName,))

        if result != ():
            self.idPlayer = result[0][0]
            self.playerName = result[0][1]
            self.lgFrame.destroy()
            self.lgFrame = LabelFrame(self.lgWindow, text=f'Welcome {playerName}', padx=10, pady=20, font=(100))
            self.lgFrame.grid(row=0, column=0, padx=200, pady=30)
            # self.lgMessage = Label(self.lgFrame, text='')
            # self.lgMessage.grid(row=6, column=0, columnspan=4, pady=10)
            Button(self.lgFrame, text='Juego Jarras', command=self.jarrasGameWindow, height=3, width=25).grid(row=0, column=0)
            Button(self.lgFrame, text='Juego Pilas', command=self.pilasGameWindow, height=3, width=25).grid(row=1, column=0)
            Button(self.lgFrame, text='Historial', command=self.historialWindow, height=3, width=25).grid(row=2, column=0)
            Button(self.lgFrame, text='Back', command=self.lgWindow.destroy, height=3, width=25).grid(row=3, column=0)

        else:
            self.lgMessage['text'] = 'Player not found'

    def jarrasGameWindow(self):

        self.count = 0
        self.jarra3 = 0
        self.jarra5 = 0

        self.lgFrame.destroy()
        self.lgWindow.title('Jarras Game')
        self.lgFrame = LabelFrame(self.lgWindow, text=f'Jarras Game', padx=15, pady=15, font=(100))
        self.lgFrame.grid(row=0, column=0, padx=135, pady=20)

        Label(self.lgFrame, text='Objetivo: Logra obtener 4 LTS en la Jarra de 5 LTS.').grid(row=0, column=0, columnspan=4, pady=10)
        Button(self.lgFrame, text='Llenar la jarra de 3 litros', command=lambda: self.jarrasGame('j3 llenar')).grid(row=1, column=0, columnspan=2, sticky=EW)
        Button(self.lgFrame, text='Llenar la jarra de 5 litros', command=lambda: self.jarrasGame('j5 llenar')).grid(row=2, column=0, columnspan=2, sticky=EW)
        Button(self.lgFrame, text='Vaciar la jarra de 3 litros', command=lambda: self.jarrasGame('j3 vaciar')).grid(row=1, column=2, columnspan=2, sticky=EW)
        Button(self.lgFrame, text='Vaciar la jarra de 5 litros', command=lambda: self.jarrasGame('j5 vaciar')).grid(row=2, column=2, columnspan=2, sticky=EW)
        Button(self.lgFrame, text='Verter el contenido de la jarra de 3 litros en la de 5 litros', command=lambda: self.jarrasGame('j3 verter')).grid(row=3, column=0, columnspan=4)
        Button(self.lgFrame, text='Verter el contenido de la jarra de 5 litros en la de 3 litros', command=lambda: self.jarrasGame('j5 verter')).grid(row=4, column=0, columnspan=4)
        Label(self.lgFrame, text='Jarra de 3 Lts -->').grid(row=5, column=0, pady=10)
        Label(self.lgFrame, text='Jarra de 5 Lts -->').grid(row=5, column=2, pady=10)

        self.jarra3Label = Label(self.lgFrame, text='')
        self.jarra3Label.grid(row=5, column=1, sticky=W)
        self.jarra5Label = Label(self.lgFrame, text='')
        self.jarra5Label.grid(row=5, column=3, sticky=W)
        self.lgMessage = Label(self.lgFrame, text='')
        self.lgMessage.grid(row=6, column=0, columnspan=4, pady=10)

        Button(self.lgFrame, text='Validar', command=lambda: self.jarrasGame('validar')).grid(row=7, column=0, columnspan=4, sticky=EW)
        Button(self.lgFrame, text='Back', command=lambda: self.loginWindow2(self.playerName)).grid(row=8, column=0, columnspan=4, sticky=EW)

    def pilasGameWindow(self):

        self.lgFrame.destroy()
        self.lgWindow.title('Pilas Game')

        self.lgFrame = LabelFrame(self.lgWindow, text='Pilas Game', padx=15, pady=15, font=(100))
        self.lgFrame.grid(row=0, column=0, padx=10, pady=30, sticky=E)
        self.lgMessage = Label(self.lgFrame, text='')
        self.lgMessage.grid(row=7, column=0, columnspan=4, pady=10)
        Label(self.lgFrame, text='Se trata de una lista con numeros del 1 al 20 desordenados.').grid(row=0, column=0, columnspan=2, sticky=W)
        Label(self.lgFrame, text='Objetivo: La suma de los ultimos elementos eliminados de una lista al azar deben ser menor o igual a 50.').grid(row=1, column=0, columnspan=2)
        Label(self.lgFrame, text='Ingresa la cantidad de elementos a quitar: ').grid(row=2, column=0, sticky=E)
        cant_elemen_quitar = Entry(self.lgFrame)
        cant_elemen_quitar.focus()
        cant_elemen_quitar.grid(row=2, column=1, sticky=W)
        Button(self.lgFrame, text='Probar suerte', height=2, width=25, command=lambda: self.pilasGame(cant_elemen_quitar.get())).grid(row=3, column=0, pady=10)
        Button(self.lgFrame, text='Back', height=2, width=25, command=lambda: self.loginWindow2(self.playerName)).grid(row=3, column=1, pady=10)
        cant_elemen_quitar.bind("<Return>", lambda e: self.pilasGame(cant_elemen_quitar.get()))
        self.label0 = Label(self.lgFrame, text='')
        self.label0.grid(row=4, columnspan=2)
        self.label1 = Label(self.lgFrame, text='')
        self.label1.grid(row=5, columnspan=2)
        self.label2 = Label(self.lgFrame, text='')
        self.label2.grid(row=6, columnspan=2)

    def historialWindow(self):

        self.lgFrame.destroy()
        self.lgWindow.title('Historial')
        self.lgFrame = LabelFrame(self.lgWindow, text=f'Historial', padx=15, pady=15, font=(100))
        self.lgFrame.grid(row=0, column=0, padx=60, pady=10)

        self.hisTree = ttk.Treeview(self.lgFrame, columns=('col1', 'col2', 'col3'))
        self.hisTree.grid(row=0, column=0, padx=20, pady=10)

        self.hisTree.heading('#0', text='Game', anchor=CENTER)
        self.hisTree.heading('col1', text='Player Name', anchor=CENTER)
        self.hisTree.heading('col2', text='Score', anchor=CENTER)
        self.hisTree.heading('col3', text='Date', anchor=CENTER)

        self.hisTree.column('#0', anchor=CENTER, width=100)
        self.hisTree.column('col1', anchor=CENTER, width=100)
        self.hisTree.column('col2', anchor=CENTER, width=100)
        self.hisTree.column('col3', anchor=CENTER, width=100)

        Button(self.lgFrame, text='Back', command=lambda: self.loginWindow2(self.playerName), height=2, width=25).grid(row=1, column=0)

        self.historial()

    def topPlayersWindow(self):

        self.tPWindow = Toplevel()
        self.tPWindow.title('Top Players')
        self.tPWindow.geometry("610x370")
        self.tPWindow.resizable(0, 0)

        self.tpFrame = LabelFrame(self.tPWindow, text=f'Top Players', padx=15, pady=15, font=(100))
        self.tpFrame.grid(row=0, column=0, padx=30, pady=10)

        self.tree = ttk.Treeview(self.tpFrame, columns=('col1', 'col2', 'col3', 'col4'))
        self.tree.grid(row=0, column=0, padx=10, pady=10)

        self.tree.heading('#0', text='Record', anchor=CENTER)
        self.tree.heading('col1', text='Game', anchor=CENTER)
        self.tree.heading('col2', text='Player Name', anchor=CENTER)
        self.tree.heading('col3', text='Score', anchor=CENTER)
        self.tree.heading('col4', text='Date', anchor=CENTER)

        self.tree.column('#0', anchor=CENTER, width=100)
        self.tree.column('col1', anchor=CENTER, width=100)
        self.tree.column('col2', anchor=CENTER, width=100)
        self.tree.column('col3', anchor=CENTER, width=100)
        self.tree.column('col4', anchor=CENTER, width=100)

        Button(self.tpFrame, text='Back', command=self.tPWindow.destroy, height=2, width=25).grid(row=1, column=0)

        self.topPlayers()

    def adminWindow(self):
        self.adWindow = Toplevel()
        self.adWindow.title('Juegos / Admin')
        self.adWindow.geometry("610x370")
        self.adWindow.resizable(0, 0)

        self.adminMessage = Label(self.adWindow, text='')
        self.adminMessage.grid(row=0, column=0, columnspan=2, pady=10)
        self.adminFrame = LabelFrame(self.adWindow, text='Admin', padx=15, pady=15, font=(100))
        self.adminFrame.grid(row=1, column=0, padx=200, pady=10)

        Label(self.adminFrame, text='User:', pady=5).grid(row=0, column=0, sticky=E)
        Label(self.adminFrame, text='Password:', pady=5).grid(row=1, column=0, sticky=E)
        userEntry = Entry(self.adminFrame)
        userEntry.focus()
        userEntry.grid(row=0, column=1, columnspan=2)
        passwordEntry = Entry(self.adminFrame, show='*')
        passwordEntry.grid(row=1, column=1, columnspan=2)

        userEntry.bind("<Return>", lambda e: passwordEntry.focus())
        passwordEntry.bind("<Return>", lambda e: self.adminWindow2(userEntry.get(), passwordEntry.get()))

        Button(self.adminFrame, text='Entry', command=lambda: self.adminWindow2(userEntry.get(), passwordEntry.get()), height=2).grid(row=2, column=0, columnspan=3, sticky=EW)
        Button(self.adminFrame, text='Back', command=self.adWindow.destroy, height=2).grid(row=3, column=0, columnspan=3, sticky=EW)

    def adminWindow2(self, user, password):

        dicc = {'sharon': '1234', 'a': 'a'}

        if user in dicc:
            if dicc[user] == password:
                self.adminFrame.destroy()
                self.adminMessage['text'] = f'Welcome {user}!'

                Button(self.adWindow, text='DELETE', command=self.detele).grid(row=1, column=0, sticky=EW)
                Button(self.adWindow, text='EDIT', command=self.editWindow).grid(row=1, column=1, sticky=EW)
                Button(self.adWindow, text='Back', command=self.adWindow.destroy, height=2, width=25).grid(row=3, column=0, columnspan=2, pady=10)

                self.adminTree = ttk.Treeview(self.adWindow, columns=('col1', 'col2', 'col3'))
                self.adminTree.grid(row=2, column=0, columnspan=2)

                self.adminTree.heading('#0', text='Player Name', anchor=CENTER)
                self.adminTree.heading('col1', text='Birthday', anchor=CENTER)
                self.adminTree.heading('col2', text='Sex', anchor=CENTER)
                self.adminTree.heading('col3', text='Email', anchor=CENTER)

                self.adminTree.column('#0', anchor=CENTER, width=150)
                self.adminTree.column('col1', anchor=CENTER, width=160)
                self.adminTree.column('col2', anchor=CENTER, width=150)
                self.adminTree.column('col3', anchor=CENTER, width=150)

                self.getRegisters()

            else:
                self.adminMessage['text'] = 'Incorrect password.'
        else:
            self.adminMessage['text'] = 'User not found.'

    def editWindow(self):

        self.adminMessage['text'] = ''
        try:
            self.adminTree.item(self.adminTree.selection())['text'][0]
        except IndexError as err:
            self.adminMessage['text'] = 'Please select a record.'
            return
        oldPlayerName = self.adminTree.item(self.adminTree.selection())['text']
        oldBirthday = self.adminTree.item(self.adminTree.selection())['values'][0]
        oldSex = self.adminTree.item(self.adminTree.selection())['values'][1]
        oldEmail = self.adminTree.item(self.adminTree.selection())['values'][2]

        self.editWind = Toplevel()
        self.editWind.title('Admin / Edit Player')
        self.editWind.geometry("400x200")
        self.editWind.resizable(0, 0)

        # Old label
        frame = LabelFrame(self.editWind, text='Edit', padx=15, pady=15, font=(100))
        frame.grid(row=0, column=0, padx=40, pady=10)
        Label(frame, text=f'PlayerName ({oldPlayerName}): ').grid(row=0, column=0, sticky=E)
        Label(frame, text=f'Birthday ({oldBirthday}): ').grid(row=1, column=0, sticky=E)
        Label(frame, text=f'Sex ({oldSex}): ').grid(row=2, column=0, sticky=E)
        Label(frame, text=f'Email ({oldEmail}): ').grid(row=3, column=0, sticky=E)

        newPlayerName = Entry(frame)
        newPlayerName.focus()
        newPlayerName.grid(row=0, column=1, columnspan=2)

        newBirthday = DateEntry(frame, date_pattern='yyyy-MM-dd')
        newBirthday.grid(row=1, column=1, columnspan=2, sticky=EW)

        newSex = StringVar()
        Radiobutton(frame, text='F', value='F', variable=newSex, indicatoron=False).grid(row=2, column=1)
        Radiobutton(frame, text='M', value='M', variable=newSex, indicatoron=False).grid(row=2, column=2)

        newEmail = Entry(frame)
        newEmail.grid(row=3, column=1, columnspan=2)
        newEmail.bind("<Return>", lambda e: self.editRecord(newPlayerName.get(), newBirthday.get_date(), newSex.get(), newEmail.get(), oldPlayerName))

        updatebutton = Button(frame, text='Update', command=lambda: self.editRecord(newPlayerName.get(), newBirthday.get_date(), newSex.get(), newEmail.get(), oldPlayerName))
        updatebutton.grid(row=4, column=0, columnspan=3, sticky=EW)

    def runQuery(self, query, args=(), bool=False):

        try:
            self.conexion = connect(
                host='localhost',
                port=3306,
                user='root',
                password='',
                database='juegos')

            cursor = self.conexion.cursor()
            cursor.execute(query, args)
            if bool:
                self.conexion.commit()
            else:
                return cursor.fetchall()

        except err.IntegrityError:
            self.message['text'] = "Player name duplicado, ingresa uno diferente."

        except Error as ex:
            self.message['text'] = f'No se pudo concretar la conexion: {ex}'

        self.conexion.close

    def getRegisters(self):

        # records = self.adminTree.get_children()
        # for record in records:
        #     self.adminTree.delete(record)

        query = "SELECT playerName, birthday, sex, email FROM player ORDER BY playerName DESC"
        result = self.runQuery(query)

        for row in result:
            self.adminTree.insert('', 0, text=row[0], values=(row[1], row[2], row[3]))

    def register(self, playerName, birthday, sex, email):

        query = "INSERT INTO player VALUES (NULL, %s, %s, %s, %s)"
        args = (playerName, birthday, sex, email)
        self.runQuery(query, args, True)
        self.message['text'] = f'Player {playerName} registered successfully!'
        self.rWindow.destroy()

    def jarrasGame(self, action):

        if action == 'j3 llenar':
            self.jarra3 = 3
            self.jarra3Label['text'] = str(self.jarra3)

        elif action == 'j5 llenar':
            self.jarra5 = 5
            self.jarra5Label['text'] = str(self.jarra5)

        elif action == 'j3 vaciar':
            self.jarra3 = 0
            self.jarra3Label['text'] = str(self.jarra3)

        elif action == 'j5 vaciar':
            self.jarra5 = 0
            self.jarra5Label['text'] = str(self.jarra5)

        elif action == 'j3 verter':
            if self.jarra5 == 5:
                self.jarra3 = 0
                self.jarra3Label['text'] = str(self.jarra3)
            else:
                self.jarra5 += self.jarra3
                if self.jarra5 <= 5:
                    self.jarra3 = 0
                    self.jarra3Label['text'] = str(self.jarra3)
                    self.jarra5Label['text'] = str(self.jarra5)
                if self.jarra5 > 5:
                    self.jarra3 = self.jarra5 - 5
                    self.jarra5 = 5
                    self.jarra3Label['text'] = str(self.jarra3)
                    self.jarra5Label['text'] = str(self.jarra5)

        elif action == 'j5 verter':
            if self.jarra3 == 3:
                self.jarra5 = 0
                self.jarra5Label['text'] = str(self.jarra5)
            else:
                self.jarra3 += self.jarra5
                if self.jarra3 <= 3:
                    self.jarra5 = 0
                    self.jarra3Label['text'] = str(self.jarra3)
                    self.jarra5Label['text'] = str(self.jarra5)
                if self.jarra3 > 3:
                    self.jarra5 = self.jarra3 - 3
                    self.jarra3 = 3
                    self.jarra3Label['text'] = str(self.jarra3)
                    self.jarra5Label['text'] = str(self.jarra5)

        elif action == 'validar':
            self.count = 10 if self.count == 6 else 9 if self.count == 7 else 8 if self.count == 8 else 7 if self.count == 9 else 6 if self.count == 10 else 5 if self.count == 11 else 4 if self.count == 12 else 3 if self.count == 13 else 2 if self.count == 14 else 1 if self.count == 15 else 0
            if self.jarra5 == 4 and self.count <= 15:
                self.lgMessage['text'] = f'Felicitaciones, lo has logrado! =D. Tu puntaje es: {self.count}'
            elif self.jarra5 == 4 and self.count > 15:
                self.lgMessage['text'] = f'Lo has logrado, pero realizaste muchos intentos! X(. Tu puntaje es: {self.count}'
            else:
                self.lgMessage['text'] = f'Mejor suerte la proxima! T_T. Tu puntaje es 0.'

            query = "INSERT INTO record VALUES (NULL, %s, %s, %s, CURDATE())"
            args = (1, self.idPlayer, self.count)
            self.runQuery(query, args, True)

        self.count += 1

    def pilasGame(self, cant_elemen_quitar):

        self.lgMessage['text'] = ''
        try:
            score = 0
            if 0 < int(cant_elemen_quitar) <= 20:
                lista_hasta_50 = []
                lista_random = list(range(1, 21))
                shuffle(lista_random)
                lista_usuario = lista_random[(20-int(cant_elemen_quitar)):21]

                while sum(lista_hasta_50) <= 50:
                    pop = lista_random.pop()
                    lista_hasta_50.append(pop)
                lista_hasta_50.pop()
                if sum(lista_usuario) > 50:
                    self.label0['text'] = f'La lista de valores al azar es: {lista_random}'
                    self.label1['text'] = f'Has perdido! Tus valores eliminados fueron {lista_usuario} y suman {sum(lista_usuario)}.'
                    self.label2['text'] = f'Los valores meta fueron {lista_hasta_50[::-1]} y suman {sum(lista_hasta_50)}. Tu puntaje es {score} =('
                else:
                    score = 10 - (len(lista_hasta_50)-len(lista_usuario))
                    self.label0['text'] = f'La lista de valores al azar es: {lista_random}'
                    self.label1['text'] = f'Has ganado! Tus valores eliminados fueron {lista_usuario} y suman {sum(lista_usuario)}.'
                    self.label2['text'] = f'Los valores meta fueron {lista_hasta_50[::-1]} y suman {sum(lista_hasta_50)}. Tu puntaje es {score} =D'

                query = "INSERT INTO record VALUES (NULL, %s, %s, %s, CURDATE())"
                args = (2, self.idPlayer, score)
                self.runQuery(query, args, True)

            else:
                self.lgMessage['text'] = 'Error: El numero de elementos a quitar debe estar entre 1 y 20.'
                self.label0['text'], self.label1['text'], self.label2['text'] = '', '', ''

        except ValueError:
            self.lgMessage['text'] = 'Error: Ingresa un numero entero entre el 1 y el 20.'
            self.label0['text'], self.label1['text'], self.label2['text'] = '', '', ''

    def historial(self):

        records = self.hisTree.get_children()
        for record in records:
            self.hisTree.delete(record)

        query = f"SELECT g.name, p.playerName, r.score, r.date FROM record r JOIN player p ON (r.idPlayer = p.idPlayer) JOIN game g ON (r.idGame = g.idGame) WHERE p.playerName = '{self.playerName}'"
        result = self.runQuery(query)

        for row in result:
            self.hisTree.insert('', 0, text=row[0], values=(row[1], row[2], row[3]))

    def topPlayers(self):

        # records = self.tree.get_children()
        # for record in records:
        #     self.tree.delete(record)

        query = "SELECT r.idRecord, g.name, p.playerName, r.score, r.date FROM record r JOIN player p ON (r.idPlayer = p.idPlayer) JOIN game g ON (r.idGame = g.idGame) ORDER BY r.score LIMIT 10"
        result = self.runQuery(query)

        for row in result:
            self.tree.insert('', 0, text=row[0], values=(row[1], row[2], row[3], row[4]))

    def detele(self):

        self.adminMessage['text'] = ''
        try:
            self.adminTree.item(self.adminTree.selection())['text'][0]
        except IndexError as err:
            self.adminMessage['text'] = 'Please select a record.'
            return

        self.adminMessage['text'] = ''
        name = self.adminTree.item(self.adminTree.selection())['text']
        query = "DELETE FROM player WHERE playerName = %s"
        self.runQuery(query, (name,), True)
        self.adminMessage['text'] = f'Record {name} deletec Successfully'

        self.getRegisters()

    def editRecord(self, newPlayerName, newBirthday, newSex, newEmail, oldPlayerName):

        query = "UPDATE player SET playerName = %s, birthday = %s, sex = %s, email = %s WHERE playerName = %s"
        parameters = (newPlayerName, newBirthday, newSex, newEmail, oldPlayerName)
        self.runQuery(query, parameters, True)
        self.editWind.destroy()
        self.adminMessage['text'] = F'Record {oldPlayerName} updated Successfully'

        self.getRegisters()


if __name__ == '__main__':
    root = Tk()
    app = Menu(root)
    root.mainloop()
