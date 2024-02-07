import React from 'react';
import IconButton from '@mui/material/IconButton';
import SyncIcon from '@mui/icons-material/Sync';

interface SyncButtonProps {
    onClick: (event: React.MouseEvent<HTMLButtonElement>) => void;
}

export default function SyncButton({ onClick }: SyncButtonProps) {
    return (
        <IconButton onClick={onClick} color="primary">
            <SyncIcon />
        </IconButton>
    );
}