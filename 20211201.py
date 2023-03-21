from python.make_routes import make_routes

make_routes("""
juletræ:Stuedørens bund
vinter:Køleskabets håndtag
abehånd:Hoveddørens hængsel
æbleskiw:Værkstedsdørens nøglehul
a-e:I den blå tusch
a-s:I den røde tusch
a-v:I den sorte tusch
a-h:I den grønne tusch
juletræ:Knobbånd over tavlen
vinter:Knobbånd bag køleskab
abehånd:Knobbånd på knagerækken
æbleskiw:Knobbånd ved udklædning
morse:Tændstikæsken ved økserne
morse:Tændstikæsken ved komfuret
morse:Tændstikæsken ved håndvasken
morse:Tændstikæsken i vindueskarmen
a-c:Under de røde kopper
a-g:Under kassen med klude
a-m:Under de blå tallerkener
a-y:Under de røde tallerkener
morse:Under trappens andet trin
morse:Under trappens første trin
morse:Under trappens tredje trin
morse:Under trappens fjerde trin
""", no_of_routes=4, show_grouped=True, rotate_routes=True)
