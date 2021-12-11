# raimundo

<p align="center">
  <img src="https://user-images.githubusercontent.com/28984561/145683268-7752772a-f6cb-459e-bb3e-38c97b171404.png" />
    <br>
    <i>A client/server application to get information about school <br>grades, aka Professor Raimundo, despite the low salary.</i>
</p>

_Raimundo_ is a client/server application responsible for grade operations. Despite the _low salary_, Raimundo makes his operations _vápiti_vúpiti_, so the communication between the client and the server is fast. 

The communication is made by a Python lib called `xmlrpc`, in which we have both **client** and **server** sides. It's worth mentioning that this works just for **Python3+**, since the `xmlrpc.client` was included on Python3+, replacing the old `xmlrpclib`.

The system has a file, a csv one, in which the grades managed. For each grade, Raimundo creates a new row on this file, containing the student registration number, the subject and the grade itself.

## The server
The server has 4 functions, at first, related to the grading system: `register_grade()`, `get_grade()`, `get_all_grades()` and `get_ac`, where

- `register_grade()`: the function, as the name suggests, registers a grade in the file. If the subject already has a registered grade, the function replaces the previous registered grade to the new one;
- `get_grade()`: receives the student registration number and a subbject and return the grade registered for that subject;
- `get_all_grades()`: as the function above, this ons also gets the registered grades from a student. However, it returns **all registered grades for every student subject.**;
- `get_ac`: last, but not least, the fucntion calculates the student's average coefficient and return to the client.

## The client
The client is quite simple: it counts with a terminal interface with some operations. Each operation is related to a server function: 
```python
{rg: register_grade(),
 gg: get_grade(),
 ga: get_all_grades(),
 ac: get_ac()}
```

## Running 
In a terminal, we gotta run 
```python3
python3 src/server.py
```
to start the server. A message like `To shutdown the server, press CTRL + C` should appear on the terminal window, indicating how to shut the server down.
Once the server is started, we gotta open a new terminal and type
```python3
python3 src/client.py
```
to start the client console. A message like 
```
Bem-vindo ao sistema de notas 2000.
As possíveis operações são:
rg - cadastrar nota(matricula, disciplina, nota)
gg - bucar nota(matricula, disciplina)
ga - buscar notas(matricula)
ac - consultar cr(matricula)
```
is shown and we can already enter an input.

The input format is almost the same as the message, but without commas or parenthesis, as follows
```
rg 2021000000 distributed-systems 9.5
```
and the function `register_grade()` is called on server with **2021000000 as the student registration number**, **distributed-systems as the subjec**t and **9.2 as the grade** itself.

To get the grades from the same student, we gotta run
```
ga 2021000000
```
