negara = {"Filiphina" : "Manila",
"Indonesia" : "Jakarta",
"Malaysia" : "Kuala Lumpur"
}
tanya = input('Tuliskan negara : ')
try :
    print(f"Ibukota {tanya} adalah {negara[tanya]}")
except KeyError :
    print(f'{tanya} gaada di dalam dictionary nih.') 