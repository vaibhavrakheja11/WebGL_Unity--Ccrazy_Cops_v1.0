using UnityEngine;
using System.Collections;

public class on_off_light : MonoBehaviour
{

	public Light[] lights;
	public KeyCode keyboard;
	public AudioSource audio;

	private bool isPlaying = false;


	void Update ()
	{
		foreach (Light light in lights)
		{
			if (Input.GetKeyDown(keyboard))
			{
				light.enabled = !light.enabled;
				//audio.Play();
			}		
		}
		if (Input.GetKeyDown(keyboard))
			{
				if(audio.isPlaying){

					audio.Pause();

				} else
				{
					audio.Play();
				}
			}

	}
}

