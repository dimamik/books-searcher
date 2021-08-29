import {StyledHeader, StyledItalic, StyledNormal} from "../../../styles/Styles";


export default function SingleBookResult({book}) {


    return <div>
        <StyledHeader>

            <span>{book.book_name}</span>

        </StyledHeader>

        <StyledHeader style={{
            position: 'absolute', right: '2vh'
        }}>
            <span>{book.book_points}</span>
        </StyledHeader>
        <StyledItalic style={{
            marginLeft: '3vh',
            marginRight: '3vh'
        }}>

            <span>{book.book_author}</span>
        </StyledItalic>
        <StyledNormal
            style={{
                marginLeft: '1vh',
                overflow: 'clip'
            }}
        >
            <span>{book.book_description}</span>

        </StyledNormal>

    </div>

}