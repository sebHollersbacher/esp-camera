import React from 'react';
import {Accordion, AccordionDetails, AccordionSummary, Typography} from "@mui/material";
import ArrowDropDownIcon from '@mui/icons-material/ArrowDropDown';

interface AllImagesProps {
    images: any[];
}

export default function AllImages({images}: AllImagesProps) {

    return (
        <div>
            {images.map((image, index) => (
                <Accordion key={index}>
                    <AccordionSummary
                        expandIcon={<ArrowDropDownIcon />}
                        aria-controls="panel-content"
                        id="panel-header"
                    >
                        <Typography>{image.replace('.jpg', '')}</Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                        <Typography>
                            <img src={image} alt='img'/>
                        </Typography>
                    </AccordionDetails>
                </Accordion>
            ))}
        </div>
    )
}