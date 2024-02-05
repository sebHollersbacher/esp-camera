import {Button} from "@mui/material";
import CameraAltIcon from '@mui/icons-material/CameraAlt';
import mqtt from "mqtt";

export default function TakeImageButton() {

    const handlePublish = () => {
        const client = mqtt.connect("ws://192.168.0.23:9001")
        client.on('connect', () => {
            console.log("connected")
            client.publish("esp_cam_0", "esp_cam_0");
            client.end();
        });
    };

    return (
        <Button
            onClick={handlePublish}
            variant="contained"
            startIcon={<CameraAltIcon />}
        >Take Pic</Button>
    )
}