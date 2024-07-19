document.addEventListener('DOMContentLoaded', function() {
    const icon = document.getElementById('pw-info-icon');
    const helptext = document.getElementById('id_password1_helptext');
    const iconElement = icon.querySelector('i');
    
    icon.addEventListener('mouseover', function() {
        helptext.style.display = 'block';
        iconElement.style.color = '#5f5f5f';
    });
    
    icon.addEventListener('mouseout', function() {
        helptext.style.display = 'none';
        iconElement.style.color = '#bebebe';
    });


    const popup = document.getElementById('popup');
    const agreeButton = document.getElementById('agree-button');
    const signupButton = document.getElementById('signup-button');
    const checkboxes = document.querySelectorAll('.agreement-checkbox');
    
    const text1Content = `
<strong>제1장 총 칙</strong><br>
<strong>제1조 (목적)</strong><br>
본 약관은 주식회사 케이티(이하 "회사")가 제공하는 AIVEX 플랫폼 관련 서비스(이하 “서비스”)를 이용함에 있어 회사와 회원과의 권리, 의무, 이용조건 및 절차에 관한 사항과 기타 이용에 필요한 사항 등을 규정함을 목적으로 합니다.

<br><strong>제2조 (약관의 효력 및 변경)</strong>
<br>1. 본 약관은 서비스를 이용하는 회원에 대하여 그 효력을 발생합니다.
<br>2. 본 약관의 내용은 AIVEX플랫폼 서비스 사이트에 게시하거나 기타의 방법으로 회원에게 공지하고, 이에 동의한 회원이 서비스에 가입함으로써 효력이 발생합니다.

<br><strong>제3조 (약관의 해석 및 약관 외 준칙)</strong>
<br>1. “회사”는 개별 서비스에 대해서 별도의 이용약관 및 운영정책을 둘 수 있으며, 해당 내용이 본 약관과 상충할 경우에는 개별 서비스 별 이용약관(이하 “개별 약관”) 또는 운영정책을 우선하여 적용합니다.

<br><strong>제4조 (용어의 정의)</strong>
<br>본 약관에서 사용하는 용어의 정의는 다음과 같습니다.
<br>1. “회원”이라 함은 회사에서 제공하는 사이트에 접속하여 본 약관과 개인정보처리방침에 동의하고, 아이디와 비밀번호를 발급받아 회사가 제공하는 서비스를 이용하는 자를 말합니다.
<br>2. “AIVEX 플랫폼”이라 함은 서비스의 제공을 위하여 회사가 구축한 AI의 이해와 데이터 수집, 전처리, 분석, AI 모델링 및 최적화를 할 수 있는 시스템을 말합니다.`;



const text2Content = `
가. 필수 수집/이용목적 및 항목
<br><br>
<table>
    <thead>
        <tr>
            <th>목적</th>
            <th>항목</th>
            <th>보유기간</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>AIVEX 일반 회원가입 및 서비스의 이용, 유지, 종료</td>
            <td>회원가입 신청인의 성명(국문 및 영문), 이메일(아이디), 비밀번호, 휴대전화번호, 성별, 생년월일, 연계정보(CI), 회사코드(기업고객에 한함)</td>
            <td>AIVEX 제공 서비스 이용기간 동안.
분쟁대비를 위해 서비스 이용기간 종료 후 6개월까지.
단, 분쟁지속시 해결시 까지 보유</td>
        </tr>
        <tr>
            <td>고지사항 전달, 서비스 제공 관련 안내, 본인의사 확인, 이용관련 문의 불만처리, 고객민원처리 등</td>
            <td>성명, 이메일(아이디), 휴대전화번호</td>
            <td>※ 예외
법령에 특별한 규정이 있을 경우 관련 법령에 따라 보관</td>
        </tr>
    </tbody>
</table>
`;

    document.getElementById('text1').innerHTML = text1Content;
    document.getElementById('text2').innerHTML = text2Content;

    agreeButton.addEventListener('click', function() {
        popup.style.display = 'none';
        signupButton.disabled = false;
    });

    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const allChecked = Array.from(checkboxes).every(cb => cb.checked);
            agreeButton.disabled = !allChecked;
        });
    });
});