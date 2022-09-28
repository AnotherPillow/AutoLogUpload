use ureq;
use std::path::Path;
use std::fs;
use std::process::Command;

fn main() {
    //load autologupload.config.json and set it to a variable
    let config = fs::read_to_string("autologupload.config.json").expect("Unable to read config file");
    
    //parse the config file
    let config: serde_json::Value = serde_json::from_str(&config).expect("Unable to parse config file");
    
    //get the log file path from the config file
    let game_path = config["game_path"].as_str().expect("Unable to get game path from config file");
    
    
    //print starting message before opening the game
    println!("Starting game...");

    std::thread::sleep(std::time::Duration::from_millis(100));

    //spawn C:\Program Files (x86)\Steam\steamapps\common\Stardew Valley\Stardew Valley.exe as a child process and run upload() when it closes


    let mut command = Command::new(game_path);
    if let Ok(mut child) = command.spawn() {
        child.wait().expect("stardew valley process failed to run");
        println!("Stardew Valley has closed, uploading log...");
        let url = upload();
        println!("Your log file has been uploaded to {}", url);
        println!("Press enter to exit");
    } else {
        println!("Failed to run Stardew Valley");
    }

    let mut input = String::new();
    std::io::stdin().read_line(&mut input).expect("Failed to read line");
}


fn upload() -> String {
    let path = Path::new(".");
    let _display = path.display();

    let p_data = std::env::var("appdata");
    let mut log_path= path.join(p_data.unwrap()).join("StardewValley").join("ErrorLogs");
    log_path.push("SMAPI-latest.txt");


    //println!("log path: {}", log_path.display());
    
    let contents = fs::read_to_string(log_path)
        .expect("Something went wrong reading the file");
    
    // let encoded = encode(contents.as_str());
    

    // let agent: Agent = ureq::AgentBuilder::new()
    //     .timeout_read(Duration::from_secs(5))
    //     .timeout_write(Duration::from_secs(5))
    //     .build();
    let response = ureq::post("https://smapi.io/log/")
        .set("Content-Type", "application.x-www-form-urlencoded")
        .send_form(&[("input", &contents)]);
    let html = response.ok().unwrap().into_string().unwrap();

    // //get the  text between </strong> <code> and </code>
    let start_bytes = html.find("</strong> <code>").unwrap_or(0);
    let end_bytes = html.find("</code>").unwrap_or(html.len());

    let res = &html[start_bytes..end_bytes].replace("</strong> <code>", "");
    //print!("{}", res);
    return res.to_string();
}