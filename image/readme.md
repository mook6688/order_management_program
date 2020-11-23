1) 프로그램 실행 시 main GUI의 기능을 하는 __init__ 함수를 실행하게 된다.
- 메인 함수에는 거래처 현황, 주문 현황 표의 틀을 잡아주는 label들과, 프로그램의 fileMenu, 개발자 정보를 담은 Aboutmenu, 실시간을 출력하는 DateintoFrame과 DB와 조작을 위한 buttonFrame을 표시하는 GUI 함수들을 담고 있다.


2) fileMenu 중 개발자 정보 클릭 시에는 clickaboutMenu를 실행하여 정보를 출력하는 틀을 만들도록 한다.

3) buttonFrame은 거래처 현황 관련 버튼, 조회, 추가, 수정, 삭제, 종료로 구성되어있다.

① 거래처현황 label 중 ‘거래처 리스트 확인 및 선택한 거래처 주문현황 조회’버튼을 눌렀을 때 companycheck() 함수를 실행하고 새로운 layout에서 원하는 거래처를 클릭 후 선택 버튼을 눌렀을 때 companycheck() 함수를 실행하고, 조회 버튼을 눌렀을 때 Check() 함수를 실행하여, 선택한 거래처명을 변수로 받아와 해당 거래처의 주문현황을 숫자로 받아오는 CompanyNumber() 함수를 실행하여 Main GUI의 조회 건수를 수정(config)한다.

 ② 추가 버튼을 눌렀을 때 Add() 함수를 실행하고 수행하게 되면 Toplevel 인 새로운 창을 닫을 수 있도록 top.destroy를 선언하기 위해 정적메소드 내 선언해준 conbine_func 함수를 이용해 command를 선언해준다. 결과는 db에도 반영되고, 해당 결과가 다시 조회한 결과에도 반영되도록 Check()를 실행해준다.

 ③ 수정 버튼을 눌렀을 때 Alter() 함수를 실행하고 수행하게 되면 Toplevel 인 새로운 창을 닫을 수 있도록 top.destroy를 선언하기 위해 정적메소드 내 선언해준 conbine_func 함수를 이용해 command를 선언해준다. 결과는 db에도 반영되고, 해당 결과가 다시 조회한 결과에도 반영되도록 Check()를 실행해준다.

 ④ 삭제 버튼을 눌렀을 때 remove() 함수를 실행하여 선택한 값이 포함된 인스턴스를 삭제할 수 있게 한다.

 ⑤ 닫기 버튼을 클릭 시 ExitProgram() 을 실행하여 ‘예’를 클릭 시 프로그램을 닫는 window.destory를 수행하고, ‘아니오’를 클릭 시 ExitProgram으로 생성된 toplevel만 닫는 top.destroy method 를 수행한다.
