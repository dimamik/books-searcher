import React, {useEffect, useState} from 'react';
import {makeStyles} from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';
import styled from "styled-components";
import {green} from "@material-ui/core/colors";
import clsx from 'clsx';
import CircularProgress from '@material-ui/core/CircularProgress';
import {StyledHeader, StyledNormal} from "../../styles/Styles";
import {addBookToFav} from "../../services/RecomService";


const useStyles = makeStyles((theme) => ({
    root: {
        display: 'flex',
        alignItems: 'center',
    },
    wrapper: {
        margin: theme.spacing(1),
        position: 'relative',
    },
    buttonSuccess: {
        backgroundColor: green[500],
        '&:hover': {
            backgroundColor: green[700],
        },
    },
    fabProgress: {
        color: green[500],
        position: 'absolute',
        top: -6,
        left: -6,
        zIndex: 1,
    },
    buttonProgress: {
        color: green[500],
        position: 'absolute',
        top: '50%',
        left: '50%',
        marginTop: -12,
        marginLeft: -12,
    },
}));


export const StyledButton = styled(Button)`
  border: 1px solid ${props => props.theme.dividerColor};
`

function LoadingButton({onClickAction, book_id}) {
    const classes = useStyles();
    const [loading, setLoading] = React.useState(false);
    const [success, setSuccess] = React.useState(false);

    const timer = React.useRef();

    const buttonClassname = clsx({
        [classes.buttonSuccess]: success,
    });
    let time = timer.current;

    React.useEffect(() => {
        return () => {
            clearTimeout(time);
        };
    }, [time]);
    const handleButtonClick = () => {
        if (!loading) {
            setSuccess(false);
            setLoading(true);
            addBookToFav(book_id).then(() => {
                setLoading(false);
                setSuccess(true);
                window.setTimeout(() => {
                    onClickAction();
                }, 200);
            });
        }

    };
    return (
        <div className={classes.root}>

            <div className={classes.wrapper}>
                <StyledButton
                    variant="contained"
                    className={buttonClassname}
                    disabled={loading}
                    onClick={handleButtonClick}
                >
                    {success ? <span>Book added</span> : <span>Select</span>}

                </StyledButton>
                {loading && <CircularProgress size={24} className={classes.buttonProgress}/>}
            </div>
        </div>
    );
}

const StyledDiv = styled.div`
  background-color: ${props => props.theme.background};
  color: ${props => props.theme.text};
`
const DialogWindow = styled.div`
  position: fixed;
  display: block;
  z-index: 100;
  top: auto;
`


export default function ChooseBookDialog({open, setOpen, selectedBook, bookSelectedAction}) {


    let [selectedBookProp, setSelectedBookProp] = useState();

    useEffect(() => {
        if (selectedBook) {
            setSelectedBookProp(selectedBook._id);
        }

    }, [selectedBook])

    // TODO Add button to select more books or go further
    const handleSelectBook = () => {
        handleClose();
        bookSelectedAction(selectedBook);
    }

    const handleClose = () => {
        setOpen(false);
    };

    return (
        <DialogWindow
        >
            <Dialog
                // fullWidth='md'
                maxWidth='md'
                open={open}
                onClose={handleClose}
                aria-labelledby="max-width-dialog-title"

            >
                <StyledDiv
                >
                    <DialogTitle id="max-width-dialog-title" style={
                        {
                            padding: '15px',
                            textAlign: 'center',
                            font: 'inherit'
                        }
                    }>

                        <img alt='close' src='https://d30y9cdsu7xlg0.cloudfront.net/png/53504-200.png' style=
                            {{
                                cursor: 'pointer',
                                position: 'absolute',
                                right: '0.5rem',
                                top: '0.5rem',
                                width: '20px',
                                marginLeft: '1vw'
                            }}
                             onClick={handleClose}
                        />
                        <StyledHeader
                            style={{
                                display: 'flex',
                                justifyContent: 'center',
                                alignItems: 'center',
                            }}
                        >
                            {selectedBook ? selectedBook._source.book_name : null}
                        </StyledHeader>
                    </DialogTitle>

                    <DialogContent

                    >
                        <StyledNormal style={
                            {
                                fontWeight: '500',
                                marginBottom: '2vh'
                            }
                        }>{selectedBook ? selectedBook._source.book_author : null}
                        </StyledNormal>

                        <DialogContentText
                            className='scrollable-content'
                            style={{
                                overflowX: 'auto',
                                height: '50vh'
                            }}
                        >
                            <StyledNormal>

                                {selectedBook ? selectedBook._source.book_description : null}</StyledNormal>


                        </DialogContentText>

                    </DialogContent>
                    <DialogActions
                        style={{
                            justifyContent: 'center'
                        }}
                    >
                        <LoadingButton
                            onClickAction={handleSelectBook}
                            book_id={selectedBookProp}
                        />

                    </DialogActions>
                </StyledDiv>
            </Dialog>
        </DialogWindow>
    );
}
