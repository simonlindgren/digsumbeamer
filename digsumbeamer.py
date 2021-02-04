#!/usr/bin/env python3

print("\nDIGSUMBEAMER\n")
projectname = input("Project name: (include .tex extension in name) ")
title = input("Presentation main title: ")
subtitle = input("Presentation subtitle: ")
author = input("Presenter name: ")

# Write basic stuff
with open(projectname, "w") as presentation:
    presentation.write("\\documentclass[aspectratio=169]{beamer}")
    presentation.write("\n")
    presentation.write("\\usepackage[utf8]{inputenc}")
    presentation.write("\n")
    presentation.write("\\usepackage[T1]{fontenc}")
    presentation.write("\n")
    presentation.write("\\usepackage[yyyymmdd]{datetime}")
    presentation.write("\n")
    presentation.write("\\usetheme{Digsum}")
    presentation.write("\n")
    presentation.write("\\usefonttheme{professionalfonts}")
    presentation.write("\n")
    presentation.write("\\title{" + title + "}")
    presentation.write("\n")
    presentation.write("\\subtitle{" + subtitle + "}")
    presentation.write("\n")
    presentation.write("\\author{" + author + "}")
    presentation.write("\n")
    presentation.write("\\logo{\includegraphics[height=1cm]{logo.png}}")
    presentation.write("\n")
    presentation.write("\\begin{document}")
    presentation.write("\n")
    presentation.write("\\begin{frame}[plain]")
    presentation.write("\n")
    presentation.write("\\maketitle")
    presentation.write("\n")
    presentation.write("\\vspace*{-1.5cm}")
    presentation.write("\n")
    presentation.write("\\hspace*{9cm}")
    presentation.write("\n")
    presentation.write("\\includegraphics[height=1.5cm]{images/logo.png}")
    presentation.write("\n")
    presentation.write("\\end{frame}")
    presentation.write("\n")

# Slide creation loop
while True:
    print("\nNew slide\n")
    slidetype = input("1 = bullets; 2 = centered; 3 = image, 0 = end: ")
    
    if slidetype == "1":
        with open(projectname, "a") as presentation:
            heading = input("Heading: ")
            presentation.write("\n")
            presentation.write("\\begin{frame}[plain]")
            presentation.write("\n")
            presentation.write("\\frametitle{"+ heading+ "}")
            presentation.write("\n")
            presentation.write("\\begin{itemize}")
            presentation.write("\n")


            while True:
                bullet = input("Bullet says: (0 = end) ")
                if bullet == "0":
                    break   
                presentation.write("\n")
                presentation.write("\\item " + bullet)
            presentation.write("\n")
            presentation.write("\n")
            presentation.write("\\end{itemize}")
            presentation.write("\n")
            presentation.write("\\end{frame}")
                
    if slidetype == "2":
        with open(projectname, "a") as presentation:
            presentation.write("\\begin{frame}[standout,plain]")
            presentation.write("\n")
            presentation.write("\\Large")
            presentation.write("\n")
            presentation.write("\n")

            while True:
                textline = input("Line says: (0 = end) ")
                if textline == "0":
                    break
                presentation.write(textline + "\\par" + "\n")
            presentation.write("\n")
            presentation.write("\n")
            presentation.write("\\end{frame}")
                
    if slidetype == "3":
        with open(projectname, "a") as presentation:
            presentation.write("\n")
            presentation.write("\\begin{frame}[plain]")
            presentation.write("\n")
            imagename = input("Imagename of png in /images/ directory: (include ,png extension in name) ")
            presentation.write("\\makebox[\linewidth]{\includegraphics[height=8cm]{images/" + imagename + "}}")
            presentation.write("\n")                         
            presentation.write("\\end{frame}")
            presentation.write("\n")

    if slidetype == "0":
                break

# End
with open(projectname, "a") as presentation:
    presentation.write("\\end{document}")
