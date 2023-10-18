import styled from "styled-components";

export const Container = styled.div`
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: relative;
    text-align: center;
`;


export const Title = styled.img`
    width: 390px;
    height: 120px;
    top: -40px;
    left: 50%;
    transform: translateX(-50%); /* 이미지를 수평으로 가운데 정렬 */
    position: absolute;
    z-index: 1;
`;

export const TitleSubText = styled.div`
    font-family: 'NanumSquareRoundEB';
    font-size: 20px;
    text-align: center;
    position: relative;
    z-index: 2;
    color: #FFFFFF;
`;

export const TitleSubTitle = styled.div`
    font-family: 'NanumSquareRoundEB';
    font-size: 30px;
    text-align: center;
    position: relative;
    z-index: 2;
    color: #FFFFFF;
    padding: 5px 0px 0px 0px;
`;

export const Logo = styled.img`
    width: 300px;
    height: 85px;
    padding: 80px 0px 50px 0px;
`;


export const Input = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
`;

export const InputID = styled.input`
    font-family: 'Pretendard';
    width: 340px;
    height: 85px;
    border: 0.5px solid black;
    border-radius: 5px;
    font-size: 25px;
    ::placeholder {
        font-family: 'Pretendard';
        font-size: 25px; 
        color: #aaaaaa; 
    }
    padding-left: 10px;
`;

export const InputPW = styled.input`
    font-family: 'Pretendard';
    width: 340px;
    height: 85px;
    border: 0.5px solid black;
    border-radius: 5px;
    font-size: 25px;
    ::placeholder {
        font-family: 'Pretendard';
        font-size: 25px; 
        color: #aaaaaa; 
    }
    padding-left: 10px;
    margin-top: 30px;
`;

export const LoginButton = styled.button`
    font-family: 'Pretendard-Bold';
    width: 350px;
    height: 65px;
    border-radius: 5px;
    border-style: none;
    font-size: 25px;
    color: white;
    background-color: #712EFF;
    margin-top: 30px;
`;

export const Join = styled.div`
    font-family: 'NotoSansKR-Bold';
    font-size: 25px;
    padding-top: 50px;
    text-decoration: underline;
`;

export const IDfinder = styled.div`
    font-family: 'NotoSansKR-Medium';
    font-size: 25px;
    padding-top: 20px;
    text-decoration: underline;
`;