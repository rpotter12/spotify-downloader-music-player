package sample;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.layout.GridPane;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import java.awt.*;
import java.io.IOException;

public class Controller {

    @FXML
    private GridPane rootPane;
    @FXML
    private Button download;
    @FXML
    private TextField musiclink;
    @FXML
    public void initialize()
    {
        download.setDisable(true);
    }
    //Stage stage;
    public void homePressed() throws IOException {
        GridPane homepane = FXMLLoader.load(getClass().getResource("sample.fxml"));
        rootPane.getChildren().setAll(homepane);
    }

    public void playlistPressed() throws IOException {
        GridPane playpane = FXMLLoader.load(getClass().getResource("playlist.fxml"));
        rootPane.getChildren().setAll(playpane);
    }

    public void settingsPressed() throws IOException {
        GridPane settingpane = FXMLLoader.load(getClass().getResource("settings.fxml"));
        rootPane.getChildren().setAll(settingpane);
    }

    public void aboutPressed() throws IOException {
        GridPane pane = FXMLLoader.load(getClass().getResource("about.fxml"));
        rootPane.getChildren().setAll(pane);
    }
    @FXML
    public void handleKeyReleased()
    {
        String text = musiclink.getText();
        boolean disableButtons = text.isEmpty() || text.trim().isEmpty();
        download.setDisable(disableButtons);
    }

}

