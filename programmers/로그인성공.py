#로그인성공?문제
#아이디와 비밀번호를 회원정보와 대조후 값을 리턴하는 함수 완성
def solution(id_pw, db):
    answer = 'fail'
    id_ = id_pw[0]
    pw = id_pw[1]
    for i in db:
        if id_ in i:
            if pw == i[1]:
                answer='login'
            else:
                answer='wrong pw'
    return answer