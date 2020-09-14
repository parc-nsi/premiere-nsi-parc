#!/usr/bin/env python3

"""
Pandoc filter to convert divs with latex="true" to LaTeX
environments in LaTeX output. The first class
will be regarded as the name of the latex environment
e.g.
<div latex="true" class="note abc">...</div>
will becomes
\begin{note}...\end{note}
"""

from pandocfilters import toJSONFilter, RawBlock, Div, stringify
import json

def latex(x):
    return RawBlock('latex', x)


def latexdivs(key, value, format, meta):
    if key == 'Div':
        [[ident, classes, kvs], contents] = value
        #if ["latex","true"] in kvs:
        #print(kvs)
        if format == "latex":
            if ident == "":
                label = ""
            else:
                label = '\\label{' + ident + '}'
            options =   ','.join('='.join(couple) for couple in kvs)
            #deboggage
            f.write(str(contents[0]['c']))
            if classes[0] == 'minipage':
                for clef, val in kvs:
                    if clef == "width":
                        options = val
                        break                
                decoupage = []
                for k in range(len(contents[0]['c'])):
                    if (contents[0]['c'][k] == {'t': 'LineBreak'} and k > 0) or (k < len(contents[0]) and contents[0]['c'][k] == {'t': 'LineBreak'} and contents[0]['c'][k-1] != {'t': 'LineBreak'}):
                        decoupage.append(k)
                i = 0
                body = [latex('\\begin{tabular}{' + 'c' * (len(decoupage) + 1) + '}')] 
                for d in decoupage:
                    body = body + [latex('\\begin{' + classes[0] + '}{' + options + '}')] +[{'t': 'Para', 'c': contents[0]['c'][i:d] }]+  [latex('\\end{' + classes[0] + '} &')]
                    i = d + 1
                body = body + [latex('\\begin{' + classes[0] + '}{' + options + '}' + label)] +[{'t': 'Para', 'c': contents[0]['c'][i:] }]+  [latex('\\end{' + classes[0] + '} \end{tabular}')]
              
            else:
                body = [latex('\\begin{' + classes[0] + '}{' + options + '}' + label)] + contents + [latex('\\end{' + classes[0] + '}')]
            if ["center","true"] in kvs:
                 left = [latex('\\begin{center}')]
                 right =  [latex('\\end{center}')]
            else:
                left = []
                right = []
            return left + body + right

f = open('sortie3.txt', 'w')

if __name__ == "__main__":
    toJSONFilter(latexdivs)

