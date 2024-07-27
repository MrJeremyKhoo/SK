import random
import db_entry
import make_title
from question_type import correctTranslation
from pylatex import Document, Package, Section, Command, Itemize, NoEscape
from pylatex.base_classes import Environment, CommandBase, Arguments, Options

# Create a new LaTeX document
doc = Document(documentclass='../exam', document_options=['addpoints, 30pt'])
doc.packages.append(Package('kotex'))
doc.packages.append(Package('verbatim'))

make_title.title(doc);

correctTranslation.make_choice(doc, db_entry.get_wordlist(), 1, 1000)

doc.generate_pdf('output', clean_tex=False)

print("PDF generated successfully!")

