towers = 22
cobras = 80
shifts = 3
cobras_total = towers * shifts
left_over = cobras - cobras_total


print "There are", towers, "Towers."
print "We have", cobras, "Cobras available."
print "We need the towers manned in", shifts,"shifts."
print "We need", cobras_total, "cobras."
print "We will therefore have an excess of", left_over, "cobras."