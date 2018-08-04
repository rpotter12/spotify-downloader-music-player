package sample;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.layout.GridPane;

import java.io.IOException;

public class playlistController {


    @FXML
    private GridPane playlistrootPane;
    //Stage stage;
    public void homePressed() throws IOException {
        GridPane homepane = FXMLLoader.load(getClass().getResource("sample.fxml"));
        playlistrootPane.getChildren().setAll(homepane);
    }

    public void playlistPressed() throws IOException {
        GridPane playpane = FXMLLoader.load(getClass().getResource("playlist.fxml"));
        playlistrootPane.getChildren().setAll(playpane);
    }

    public void settingsPressed() throws IOException {
        GridPane settingpane = FXMLLoader.load(getClass().getResource("settings.fxml"));
        playlistrootPane.getChildren().setAll(settingpane);
    }

    public void aboutPressed() throws IOException {
        GridPane pane = FXMLLoader.load(getClass().getResource("about.fxml"));
        playlistrootPane.getChildren().setAll(pane);
    }



}
