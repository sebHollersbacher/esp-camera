import React from 'react';
import {Accordion, AccordionDetails, AccordionSummary, Typography} from "@mui/material";
import ArrowDropDownIcon from '@mui/icons-material/ArrowDropDown';
import Image from "./Image";
import '../styles/ImageList.css';

interface ImageListProps {
    images: any[];
}

export default function ImageList({images}: ImageListProps) {

    return (
        <div className="center-container">
            {images.map((image, index) => (
                <Accordion key={index} className="weighted-accordion">
                    <AccordionSummary
                        expandIcon={<ArrowDropDownIcon />}
                        aria-controls="panel-content"
                        id="panel-header"
                    >
                        <Typography>{image.replace('.jpg', '')}</Typography>
                    </AccordionSummary>
                    <AccordionDetails>
                        <Typography>
                            <Image image={image} />
                        </Typography>
                    </AccordionDetails>
                </Accordion>
            ))}
        </div>
    )
}