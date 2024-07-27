import db_entry
import time
import make_title
from question_type import correctTranslation, 이에요, 은는, 은는이에요
from pylatex import Document, Package, Section, Command, Itemize, NoEscape
from pylatex.base_classes import Environment, CommandBase, Arguments, Options


def switch_case(case, doc, words):
    match case:
        case "translation":
            correctTranslation.make_choice(doc, db_entry.get_translatelist(words), 1, 30)
            return "Case for Translation executed"
        case "은/는":
            은는.make_choice(doc, db_entry.get_nounlist(words),1, 30)
            return "Case for 은/는 executed"
        case "예요/이에요":
            이에요.make_choice(doc, db_entry.get_nounlist(words),1, 30)
            return "Case for 예요/이에요 executed"
        case "은/는예요/이에요":
            은는이에요.make_choice(doc, db_entry.get_nounlist(words),1, 100)
            return "Case for 은/는예요/이에요 executed"
        case _:
            return "Default case executed"

def main(topic, words):
    # Create a new LaTeX document
    doc = Document(documentclass='../exam', document_options=['addpoints, 30pt'])
    doc.packages.append(Package('kotex'))
    doc.packages.append(Package('verbatim'))

    make_title.title(doc)

    for question_type in topic:
        switch_case(question_type, doc, words)

    pdf_path = 'output.pdf'
    doc.generate_pdf('output', clean_tex=False)

    print("PDF generated successfully!")
    return pdf_path

if __name__ == "__main__":
    main(["translation"], ['도시', '이름', '저', '나', '남자', '여자', '이', '그', '저', '것', '이것', '그것', '저것', '의자', '탁자', '선생님', '침대', '집', '차', '사람', '책', '컴퓨터', '나무', '소파', '중국', '일본', '문', '의사', '학생', '이다', '네', '아니', '나라', '가방', '창문', '잡지', '방', '냉장고', '개', '강아지', '고양이', '쥐', '펜', '전화기', '커피', '식당', '건물', '텔레비전', '미국', '캐나다', '호텔', '학교', '은행', '안', '위', '밑', '옆', '뒤', '앞', '여기', '있다', '있다', '음식', '케이크', '공항', '병원', '공원', '한국어', '머리', '귀', '팔', '눈', '입', '배', '버스', '배', '우리', '먹다', '가다','만나다', '닫다', '열다', '원하다', '만들다', '하다', '말하다', '이해하다', '좋아하다', '크다','작다', '새롭다', '낡다', '비싸다', '싸다', '아름답다', '뚱뚱하다', '길다', '좋다'])
