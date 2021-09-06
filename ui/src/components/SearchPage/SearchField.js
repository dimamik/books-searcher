import React from 'react';
import IconButton from '@material-ui/core/IconButton';
import SearchIcon from '@material-ui/icons/Search';
import {Grid} from "@material-ui/core";
import {StyledInputBase} from "../../styles/Styles";


export default function SearchField({
                                        handleSearchAsYouType,
                                        triggerSearchBar,
                                        handleSearchButton,
                                        searchQueryProp
                                    }) {

    let [searchQuery, setSearchQuery] = searchQueryProp

    const handleInputChange = (event) => {
        let value = event.target.value
        setSearchQuery(value);
        handleSearchAsYouType(value);
    }

    const handleClick = () => {
        triggerSearchBar();
    }

    const searchClicked = () => {
        handleSearchButton(searchQuery);
    }

    return (

        <Grid
            justifyContent="center"
            alignItems="center"
            container
        >
            <Grid xs={10}
                  item
                  style={{textAlign: 'left', paddingLeft: '5vw'}}
            >
                <StyledInputBase
                    placeholder="Find your favorite book"
                    value={searchQuery}
                    onChange={handleInputChange}
                    onFocus={handleClick}
                    onBlur={handleClick}
                />
            </Grid>

            <Grid
                xs={2}
                item
            >
                <IconButton
                    onClick={searchClicked}
                    style={{
                        float: 'right',
                        paddingRight: '2vw'
                    }}
                    aria-label="search">
                    <SearchIcon/>
                </IconButton>
            </Grid>
        </Grid>
    );
}
