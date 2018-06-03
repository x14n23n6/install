do
SetText("Hacked")
set Objvoice = 
CreateObject("SAPI.Spvoice")
Objvoice.Rate =-3
Objvoice.Speak SetText
loop
