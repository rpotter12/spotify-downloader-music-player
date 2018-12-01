package com.rohit.sdmp;

import javafx.event.ActionEvent;
import javafx.event.EventHandler;
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

    // method for working of spotdl command
    public void downloadSong() throws IOException {
        Runtime rt = Runtime.getRuntime();
        Process proc = rt.exec("spotdl -s "+musiclink.getText());

        BufferedReader stdInput = new BufferedReader(new
                InputStreamReader(proc.getInputStream()));

        BufferedReader stdError = new BufferedReader(new
                InputStreamReader(proc.getErrorStream()));

        // read the output from the command
        String s = null;
        while ((s = stdInput.readLine()) != null) {
            System.out.println(s);
        }

        while ((s = stdError.readLine()) != null) {
            System.out.println(s);
        }

//         to check command string
//         System.out.println(commands);
    }
}

