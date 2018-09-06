package com.rohit.sdmp;

import javafx.concurrent.Task;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.layout.GridPane;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class homeController {

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
        GridPane homepane = FXMLLoader.load(getClass().getResource("home.fxml"));
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


    public void downloadSong() throws IOException{
        downloadSong();
    
    }
    public void downloadSong(ActionEvent actionEvent) {
        String command = "python3 spotdl.py --song " + musiclink;
        Task<String> commandTask = new Task<String>() {
            @Override
            protected String call() {
                return executecmd(command);
            }
        };
    }

    private String executecmd(String command) {
        StringBuffer output = new StringBuffer();
        Process p;
        try {
            p = Runtime.getRuntime().exec("/usr/share/applications/Terminal"+command);
            p.waitFor();
            BufferedReader reader =
                    new BufferedReader(new InputStreamReader(p.getInputStream()));
            String line = "";
            while ((line = reader.readLine())!= null) {
                output.append(line + "\n");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return output.toString();
    }
}

